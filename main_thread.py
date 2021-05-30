import threading
import mysql.connector as sql
from sql_thread_functions import *
from time import sleep
from stock_functions import *


#--------------------------------------------------------------------------------------
def thread_loop():
    
    #CREATE THE SQL CONNECTION FOR THE THREAD
    sqlThreadFunctions.createDBcon(sqlThreadFunctions)

    #THE MAIN THREAD
    while True:
        
        #add all company tickers to company dictionary from DB
        sqlThreadFunctions.refreshDBCompanyDictionary(sqlThreadFunctions)
        print(databaseCompanyList)

        #iterate all the values in the dict and update db
        for i in databaseCompanyList.keys():
            result = stockFunctions.returnCompanyDetails(stockFunctions, i)
            print(result)
            sqlThreadFunctions.updateRecord(sqlThreadFunctions, i, result[0], result[1], result[2], result[3], result[4])

        #update db from json lists
        sqlThreadFunctions.refreshJsonData(sqlThreadFunctions)
        sqlThreadFunctions.add_to_database(sqlThreadFunctions)
        sqlThreadFunctions.remove_from_database(sqlThreadFunctions)

        #reset json
        sqlThreadFunctions.clearJson(sqlThreadFunctions, "companyList.json")
        sleep(0.5)
        
    
if __name__ == '__main__':
    sqlthread = threading.Thread(target=thread_loop)
    sqlthread.start()
    

# class func1(Thread):
    
#     def __init__(self,Ticker,companyName):
#       Thread.__init__(self)
      
#       self.Ticker = Ticker
#       self.companyName=companyName
      
    
    
#     def run(self):
#         while True:
#             print(stockFunctions.returnCompanyDetails(self, self.Ticker, self.companyName))
#             sleep(20)

# def thread_loop():
#   for i in threadlist:
#       a,b=i
#       thread=func1(a,b)
#       thread.start()
#       sleep(3)

#__main__
# companyName=input()
# Ticker=stockFunctions.returnTickerSymbol(stockFunctions,companyName)
# threadlist.append((Ticker,companyName))
# thread_loop()