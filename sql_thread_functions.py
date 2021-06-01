import json
import requests
from time import sleep
import yfinance as yf
import mysql.connector as sql
import mysql.connector.errors as Error
from main_thread import *

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
            with open('companyList.json') as f:
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
                companyName = sqlThreadFunctions.returnCompanyName(self, i[1])
                if(companyName == "skip123"):
                    continue
                newData.append(companyName)
                newData.append(sqlThreadFunctions.returnTickerSymbol(self, str(newData[0]).split()[0].replace(",", "")))
                additems_list_filtered.append(newData)
            elif((len(i) > 1) and ("lol123" in str(i[1]))):
                print("searched by name")
                newData = []
                newData.append(i[0])
                ticker = sqlThreadFunctions.returnTickerSymbol(self, newData[0])
                if (ticker == "skip123"):
                    continue
                newData.append(sqlThreadFunctions.returnCompanyName(self, ticker))
                newData.append(ticker)
                newData.pop(0)
                additems_list_filtered.append(newData)
        additems_list.clear()


    def updateRecord(self, ticker, currentPrice, change, changeP, Open, close):
        cmd = '''UPDATE companydata SET S_CurrentPrice = %s, S_Change = %s, S_ChangeP = %s, S_Open = %s, S_PreviousClose = %s WHERE S_Ticker = %s;'''
        sqlCur.execute(cmd, (currentPrice, change, changeP, Open, close, ticker))
        con.commit()

    def add_to_database(self):
        for i in additems_list_filtered:
            companyName = (str(i[0]))
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
            company = i[0]
            cmd = "DELETE FROM companyData WHERE S_Company = '{}';".format(company)
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
        databaseCompanyList.clear()
        cmd = "select * from companydata;"
        sqlCur.execute(cmd)
        data = sqlCur.fetchall()
        for i in data:
            databaseCompanyList[i[0]] = i[1]
    
    def returnTickerSymbol(self, CompanyName):
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=" + CompanyName + "&lang=en"
        r = requests.get(url)
        try:
            return r.json()["ResultSet"]["Result"][0]["symbol"]
        except IndexError:
            print(f"No company called {CompanyName} exists")
            return ("skip123")

    def returnCompanyName(self, ticker):
        try:
            return(yf.Ticker(ticker).info["longName"])
        except KeyError:
            print(f"Company {ticker} not found!")
            return ("skip123")