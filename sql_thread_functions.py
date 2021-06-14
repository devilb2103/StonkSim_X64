import json
import requests
from time import sleep
import yfinance as yf
import mysql.connector as sql
import mysql.connector.errors as Error
from main_thread import *
import os
import csv

additems_list = []
additems_list_filtered = []
remitems_list = []
databaseCompanyList = {}
con = None
sqlCur = None

currentTable = ""

class sqlThreadFunctions():

    def createDBcon(self):
        global con
        global sqlCur
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
    
    def readCurrentTableFromFile(self):
        global currentTable
        try:
            file = open("tableName.txt", "r")
            text = file.read()
            currentTable = str(text).split()[0]
            file.close()
            os.remove("tableName.txt")
        except Exception as e:
            print(e)
    
    def getCurrentTable(self):
        return currentTable

    ## CLEARS FIRST LINE OF JSON SO THAT UNICODE CHARS CAN BE REWRITTEN
    def clearFirstLine(self, filename):
        with open(filename) as f: 
            lines = f.readlines() #read 
        #modify 
        lines[0] = "{\n" #you can replace zero with any line number. 
        with open(filename, "w") as f: 
            f.writelines(lines) #write back 
    
    def writeToCSV(self, data):
        try:
            with open("tickerList.csv", "a", newline="") as CSVfile:
                writer = csv.writer(CSVfile)
                if(not(len(data) == 0)):
                    if(not(sqlThreadFunctions.readFromCSV(self, data[0], 1))):
                        writer.writerow(data[0])
                CSVfile.close()
        except Exception as e:
            print(e)
    
    #reads from csv file
    def readFromCSV(self, query, mode):
        try:
            with open("tickerList.csv", "r") as CSVfile:
                csvDataRaw = csv.reader(CSVfile)
                csvData = list(csvDataRaw)
                #returns ticker/company for entered company/ticker
                if(mode == 0):
                    for companyDetails in csvData:
                        if(query.lower() in [str(companyDetails[0]).lower(), str(companyDetails[1]).lower()]):
                            if(query.lower() in str(companyDetails[0]).lower()):
                                return(companyDetails[1])
                            return(companyDetails[0])
                    pass
                #returns bool for existing entered company or ticker
                if(mode == 1):
                    for companyDetails in csvData:
                        if(query == companyDetails):
                            return(True)
                    return(False)

        except Exception as e:
            print(e)

    ## REFRSHES THE LISTS THAT CONTAIN 
    def refreshJsonData(self):

        global additems_list
        global remitems_list

        try:
            with open('companyList.json') as f:
                try:
                    data = json.load(f)
                    ##add list
                    add_dict = data['add']
                    additems_list = list(add_dict.items())
                    ##remove list
                    rem_dict = data['remove']
                    remitems_list=list(rem_dict.items())
                    #close
                    f.close()
                except json.JSONDecodeError:
                    print("json decode error")
                    pass

        except FileNotFoundError:
            print("no json file!")
    
    def FilterRetrievedData(self):
        for i in additems_list:
            if((len(i) > 1) and ("lol123" in str(i[0]))):
                print("searched by ticker")
                companyName = ""
                
                #checks if the data we need is already in csv because file reading is faster than internet data retrieval lol
                if(sqlThreadFunctions.readFromCSV(self, str(i[1]).upper(), 0)):
                    companyName = (sqlThreadFunctions.readFromCSV(self, str(i[1]).upper(), 0))
                
                newData = []
                #checks if companyName var already has data read from csv, otherwise it queries from internet
                if(companyName == ""):
                    companyName = sqlThreadFunctions.returnCompanyName(self, i[1])
                    if(companyName == "skip123"):
                        print(i[1])
                        continue
                
                #adding stuff to filtered add items list
                newData.append(companyName)
                newData.append(str(i[1]).upper())
                additems_list_filtered.append(newData)
            
            elif((len(i) > 1) and ("lol123" in str(i[1]))):
                print("searched by name")
                newData = []
                newData.append(i[0])

                ticker = ""
                #checks if the data we need is already in csv because file reading is faster than internet data retrieval lol
                if(sqlThreadFunctions.readFromCSV(self, newData[0], 0)):
                    ticker = (sqlThreadFunctions.readFromCSV(self, newData[0], 0))
                
                #checks if ticker var already has data read from csv, otherwise it queries from internet
                if(ticker == ""):
                    ticker = sqlThreadFunctions.returnTickerSymbol(self, newData[0])
                    if (ticker == "skip123"):
                        continue

                companyName = ""
                #checks if the data we need is already in csv because file reading is faster than internet data retrieval lol
                if(sqlThreadFunctions.readFromCSV(self, ticker, 0)):
                    companyName = (sqlThreadFunctions.readFromCSV(self, ticker, 0))

                #checks if companyname var already has data read from csv, otherwise it queries from internet
                if(companyName == ""):
                    newData.append(sqlThreadFunctions.returnCompanyName(self, ticker))
                else:
                    newData.append(companyName)

                newData.append(ticker)
                newData.pop(0)
                additems_list_filtered.append(newData)
        additems_list.clear()


    def updateRecord(self, localTableName, ticker, currentPrice, change, changeP, Open, close):
        cmd = f"UPDATE {localTableName} SET S_CurrentPrice = %s, S_Change = %s, S_ChangeP = %s, S_Open = %s, S_PreviousClose = %s WHERE S_Ticker = %s;"
        sqlCur.execute(cmd, (currentPrice, change, changeP, Open, close, ticker))
        con.commit()

    def add_to_database(self):
        for i in additems_list_filtered:
            companyName = (str(i[0]))
            ticker = i[1]
            cmd = f"INSERT INTO {currentTable} (S_Ticker, S_Company) VALUES(%s,%s)"
            try:
                sqlCur.execute(cmd, (ticker, companyName))
            except Error.IntegrityError as e:
                print("multiple entries lol", e)
            con.commit()
        sqlThreadFunctions.writeToCSV(self, additems_list_filtered)
        additems_list_filtered.clear()

    def remove_from_database(self):
        for i in remitems_list:
            company = i[0]
            cmd = "DELETE FROM {} WHERE S_Company = '{}';".format(currentTable, company)
            sqlCur.execute(cmd)
            con.commit()
    
    def removeNoneCompanies(self):
        cmd = "DELETE FROM {} WHERE S_Company = '{}';".format(currentTable, None)
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
        global currentTable
        databaseCompanyList.clear()
        cmd = f"select * from {currentTable};"
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