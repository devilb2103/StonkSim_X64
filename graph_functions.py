import yfinance as yf
from time import sleep
import requests
import mysql.connector as sql
from PySide2 import QtCore, QtGui

from ui_main import Ui_MainWindow

con = None
sqlCur = None

class GraphFunctions():
    
    dataLine = None
    xData = []
    yData = []
    toSearchCursor = ""
    searchType = 0

    killDataFetcherThread = False

    def initDB(self):
        global con
        global sqlCur
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
    
    def initGraph(self):
        self.ui.graph_widget.setBackground(QtGui.QColor(35, 35, 35))
        GraphFunctions.dataLine = self.ui.graph_widget.plot() #takes 2 lists

    def getCurrentPrice(self, ticker):
        YFcursor = yf.Ticker(ticker)
        data = YFcursor.history(period='max')
        return list(round((data['Close'])[0:-1], 2))

    def getCompanyList(self):
        cmd = "SELECT S_Ticker, S_Company FROM companydata;"
        if(sqlCur != None):
            sqlCur.execute(cmd)
            companyList = sqlCur.fetchall()
            companyDict = {}
            for i in companyList:
                companyDict[i[1]] = i[0]
            return companyDict
        else:
            print("faulty con")
    
    def getGraphHistory(self, ticker, mode):
        YFcursor = yf.Ticker(ticker)
        if(mode == 0):
            data = yf.download(ticker,period='1d',interval='1m')
            return data['Open']
        elif (mode == 1):
            data = yf.download(ticker,period='5d',interval='1h')
            return data['Open']
        elif (mode == 2):
            data = yf.download(ticker,period='max')
            return data['Open']
    
    #===============================================================================================
    ##UPDATE-TIMER

    def graphTimer(self):
        #DO GRAPH STUFF HERE
        while not(GraphFunctions.killDataFetcherThread):
            if(GraphFunctions.toSearchCursor != ""):
                data = GraphFunctions.getGraphHistory(self, GraphFunctions.toSearchCursor, GraphFunctions.searchType)
                GraphFunctions.xData, GraphFunctions.yData = list(data), list(data)
            sleep(0.25)