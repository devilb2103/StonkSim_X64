import json
import requests
import yfinance as yf
import os

class JSONFuntions():

    def createJSON(self):
        file = open("companyList.json", "w")
        file.truncate()
        initStuct = {
            "add":{},
            "remove":{}
        }
        file.write(json.dumps(initStuct, indent=4))
        file.close()

    def writeToCompanyList(self, companyName, ticker, writeState):
        if(writeState):
            #write in to - add list
            with open("companyList.json", "r+") as file:
                data = json.load(file)
                data["add"][companyName] = ticker
                file.truncate(0)
                file.write(json.dumps(data, indent=4))
                file.close()
        else:
            #write in to - remove list
            with open("companyList.json", "r+") as file:
                data = json.load(file)
                data["remove"][companyName] = ticker
                file.truncate(0)
                file.write(json.dumps(data, indent=4))
                file.close()
        JSONFuntions.clearFirstLine(self, "companyList.json")
    
    
    def clearFirstLine(self, filename):
        with open(filename) as f: 
            lines = f.readlines() #read 
        #modify 
        lines[0] = "{\n" #you can replace zero with any line number. 
        with open(filename, "w") as f: 
            f.writelines(lines) #write back 

    def deleteJson(self):
        os.remove("companyList.json")
    
    def initJSON(self):
        self.createJSON()

    def returnTickerSymbol(self, CompanyName):
        url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=" + CompanyName + "&lang=en"
        r = requests.get(url)
        return r.json()["ResultSet"]["Result"][0]["symbol"]

    def returnCompanyName(self, ticker):
        return(yf.Ticker(ticker).info["longName"])