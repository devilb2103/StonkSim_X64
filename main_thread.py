
import multiprocessing
import mysql.connector as sql
from sql_thread_functions import *
from time import sleep
from stock_functions import *

processList = {}

class mainThread():

    def instantiateCompanyProcess(self, ticker):
        p = multiprocessing.Process(target=self.companyProcess, args=(self, ticker,))
        p.start()
        processList[str(ticker)] = p

    def companyProcess(self, ticker):
        sqlThreadFunctions.createDBcon(sqlThreadFunctions)
        while True:
            #print(f"running company Process: {ticker}")
            try:
                result = stockFunctions.returnCompanyDetails(stockFunctions, ticker)
                sqlThreadFunctions.updateRecord(sqlThreadFunctions, ticker, result[0], result[1], result[2], result[3], result[4])
            except Exception as e:
                print(e)

    def removeProcess(self):
        processes = list(processList.keys())
        tickers = list(databaseCompanyList.keys())
        for processName in processes:
            if(not (processName in tickers)):
                #print(f"unwanted process {processName} removed")
                processList[processName].terminate()
                processList.pop(processName)

    #--------------------------------------------------------------------------------------
    def thread_loop(self):
        
        #CREATE THE SQL CONNECTION FOR THE THREAD
        sqlThreadFunctions.createDBcon(sqlThreadFunctions)

        #THE MAIN THREAD
        while True:
            #add all company tickers to company dictionary from DB
            sqlThreadFunctions.refreshDBCompanyDictionary(sqlThreadFunctions)

            #iterate all the values in the dict and update db
            for ticker in databaseCompanyList.keys():
                if(len(processList.keys()) > 0):
                    canCreateProcess = True
                    #print(processList.keys())
                    for process in processList.keys():
                        if (process.startswith(str(ticker))):
                            canCreateProcess = False
                    if(canCreateProcess):
                        self.instantiateCompanyProcess(self, ticker)
                else:
                    self.instantiateCompanyProcess(self, ticker)
            
            ##processes are annihilated here
            self.removeProcess(self)

            #update db from json lists
            sqlThreadFunctions.FilterRetrievedData(sqlThreadFunctions)
            sqlThreadFunctions.add_to_database(sqlThreadFunctions)
            sqlThreadFunctions.remove_from_database(sqlThreadFunctions)
            sqlThreadFunctions.removeNoneCompanies(sqlThreadFunctions)
                ## refresh json data after heavy tasks AND BEFORE clear json data so program does not miss out inputs
            sqlThreadFunctions.refreshJsonData(sqlThreadFunctions)
            #reset json
            sqlThreadFunctions.clearJson(sqlThreadFunctions, "companyList.json")
            sleep(0.25)
            
        
if __name__ == '__main__':
    mainThread.thread_loop(mainThread)