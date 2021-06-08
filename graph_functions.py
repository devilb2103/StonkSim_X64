import yfinance as yf
from time import sleep
import requests
import datetime
import mysql.connector as sql
from PySide2 import QtCore, QtGui
import numpy as np

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
        if (mode == 0):
            start, end = datetime.datetime.now() - datetime.timedelta(days=7), datetime.datetime.now()
            data = yf.download(ticker, start=start, end=end, interval="30m")
            GraphFunctions.xData = np.linspace(1, 7, len(dict(data)["Open"]))
            return data['Open']
        elif (mode == 1):
            start, end = datetime.datetime.now() - datetime.timedelta(days=30), datetime.datetime.now()
            data = yf.download(ticker, start=start, end=end, interval="1d")
            GraphFunctions.xData = np.linspace(1, 30, len(dict(data)["Open"]))
            return data['Open']
        elif (mode == 2):
            start, end = datetime.datetime.now() - datetime.timedelta(days=180), datetime.datetime.now()
            data = yf.download(ticker, start=start, end=end, interval="1d")
            GraphFunctions.xData = np.linspace(1, 180, len(dict(data)["Open"]))
            return data['Open']
        elif (mode == 3):
            start, end = datetime.datetime.now() - datetime.timedelta(days=365), datetime.datetime.now()
            data = yf.download(ticker, start=start, end=end, interval="1d")
            GraphFunctions.xData = np.linspace(1, len(dict(data)["Open"]), len(dict(data)["Open"]))
            return data['Open']
        elif (mode == 4):
            start, end = datetime.datetime.now() - datetime.timedelta(days=1825), datetime.datetime.now()
            data = yf.download(ticker, start=start, end=end, interval="1wk")
            GraphFunctions.xData = np.linspace(1, len(dict(data)["Open"]), len(dict(data)["Open"]))
            return data['Open']
        elif (mode == 5):
            data = yf.download(ticker, period="max", interval="1d")
            GraphFunctions.xData = np.linspace(1, len(dict(data)["Open"]), len(dict(data)["Open"]))
            return data['Open']
    
    #===============================================================================================
    ##UPDATE-TIMER

    def graphThread(self):
        #DO GRAPH STUFF HERE
        while not(GraphFunctions.killDataFetcherThread):
            if(GraphFunctions.toSearchCursor != ""):
                data = GraphFunctions.getGraphHistory(self, GraphFunctions.toSearchCursor, GraphFunctions.searchType)
                GraphFunctions.yData = list(data)
            sleep(0.25)