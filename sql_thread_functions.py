import json
import mysql.connector as sql
import mysql.connector.errors as Error

additems_list = []
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
            #Code goes here:-
            add_dict = data['add']
            additems_list = list(add_dict.items())
            rem_dict = data['remove']
            remitems_list=list(rem_dict.items())
            f.close()
        except FileNotFoundError:
            print("no json file!")

    def updateRecord(self, ticker, currentPrice, change, changeP, Open, close):
        cmd = '''UPDATE companydata SET S_CurrentPrice = %s, S_Change = %s, S_ChangeP = %s, S_Open = %s, S_PreviousClose = %s WHERE S_Ticker = %s;'''
        sqlCur.execute(cmd, (currentPrice, change, changeP, Open, close, ticker))
        con.commit()

    def add_to_database(self):
        for i in additems_list:
            companyName = (str(i[0]).split()[0]).replace(",", "")
            ticker = i[1]
            cmd = "INSERT INTO companydata (S_Ticker, S_Company) VALUES(%s,%s)"
            try:
                sqlCur.execute(cmd, (ticker, companyName))
            except Error.IntegrityError:
                print("multiple entries lol")
            con.commit()

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
        data2 = sqlCur.fetchall()
        for i in data2:
            databaseCompanyList[i[0]] = i[1]

if __name__ == '__main__':
    from stock_functions import *
    sqlThreadFunctions.createDBcon(sqlThreadFunctions)
    result = stockFunctions.returnCompanyDetails(stockFunctions, "GOOG")
    print(type(result[0]), result[1], result[2], result[3], result[4])
    sqlThreadFunctions.updateRecord(sqlThreadFunctions, result[0], result[1], result[2], result[3], result[4], "GOOG")
    