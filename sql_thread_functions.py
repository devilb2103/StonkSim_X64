import json
import requests
from time import sleep
import yfinance as yf
import mysql.connector as sql
import mysql.connector.errors as Error

additems_list = []
additems_list_filtered = []
remitems_list = []
databaseCompanyList = {}
con = None
sqlCur = None


class sqlThreadFunctions():

    def createDBcon(self):
        global con
        global sqlCur
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
    
    ## CLEARS FIRST LINE OF JSON SO THAT UNICODE CHARS CAN BE REWRITTEN
    def clearFirstLine(self, filename):
        with open(filename) as f: 
            lines = f.readlines() #read 
        #modify 
        lines[0] = "{\n" #you can replace zero with any line number. 
        with open(filename, "w") as f: 
            f.writelines(lines) #write back 

    ## REFRSHES THE LISTS THAT CONTAIN 
    def refreshJsonData(self):

        global additems_list
        global remitems_list

        try:
            f = open('companyList.json')
            data = json.load(f)
            ##add list
            add_dict = data['add']
            additems_list = list(add_dict.items())
            
            ##remove list
            rem_dict = data['remove']
            remitems_list=list(rem_dict.items())
            #close    
            f.close()
        
        except FileNotFoundError:
            print("no json file!")
    
    def FilterRetrievedData(self):
        for i in additems_list:
            if((len(i) > 1) and ("lol123" in str(i[0]))):
                print("searched by ticker")
                newData = []
                newData.append(sqlThreadFunctions.returnCompanyName(self, i[1]))
                newData.append(sqlThreadFunctions.returnTickerSymbol(self, str(newData[0]).split()[0].replace(",", "")))
                additems_list_filtered.append(newData)
                print(additems_list_filtered)
            elif((len(i) > 1) and ("lol123" in str(i[1]))):
                print("searched by name")
                newData = []
                newData.append(i[0])
                ticker = sqlThreadFunctions.returnTickerSymbol(self, newData[0])
                newData.append(sqlThreadFunctions.returnCompanyName(self, ticker))
                newData.append(ticker)
                newData.pop(0)
                additems_list_filtered.append(newData)
                print(additems_list_filtered)
        additems_list.clear()


    def updateRecord(self, ticker, currentPrice, change, changeP, Open, close):
        cmd = '''UPDATE companydata SET S_CurrentPrice = %s, S_Change = %s, S_ChangeP = %s, S_Open = %s, S_PreviousClose = %s WHERE S_Ticker = %s;'''
        sqlCur.execute(cmd, (currentPrice, change, changeP, Open, close, ticker))
        con.commit()

    def add_to_database(self):
        for i in additems_list_filtered:
            companyName = (str(i[0]))
            #companyName = (str(i[0]).split()[0]).replace(",", "")
            ticker = i[1]
            cmd = "INSERT INTO companydata (S_Ticker, S_Company) VALUES(%s,%s)"
            try:
                sqlCur.execute(cmd, (ticker, companyName))
            except Error.IntegrityError as e:
                print("multiple entries lol", e)
            con.commit()
        additems_list_filtered.clear()

    def remove_from_database(self):
        for i in remitems_list:
            ticker=i[1]
            cmd="DELETE FROM companyData WHERE S_Ticker = '{}'".format(ticker);
            sqlCur.execute(cmd)
            con.commit()
            
    def clearJson(self, file):
        try:
            file = open(file, "r+")
            file.truncate()
            initStuct = {
                "add":{},
                "remove":{}
            }
            file.write(json.dumps(initStuct, indent=4))
            file.close()
        except:
            print("no json file!")

    def refreshDBCompanyDictionary(self):
        global databaseCompanyList
        cmd = "select * from companydata;"
        sqlCur.execute(cmd)
        data = sqlCur.fetchall()
        for i in data:
            databaseCompanyList[i[0]] = i[1]
    
    def returnTickerSymbol(self, CompanyName):
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=" + CompanyName + "&lang=en"
        r = requests.get(url)
        return r.json()["ResultSet"]["Result"][0]["symbol"]
        # try:
        #     return r.json()["ResultSet"]["Result"][0]["symbol"]
        # except Exception:
        #     print("failed to return ticker symbol for company name input: ", CompanyName)

    def returnCompanyName(self, ticker):
        return(yf.Ticker(ticker).info["longName"])

if __name__ == '__main__':
    from stock_functions import *
    sqlThreadFunctions.createDBcon(sqlThreadFunctions)
    result = stockFunctions.returnCompanyDetails(stockFunctions, "GOOG")
    print(type(result[0]), result[1], result[2], result[3], result[4])
    sqlThreadFunctions.updateRecord(sqlThreadFunctions, result[0], result[1], result[2], result[3], result[4], "GOOG")
    