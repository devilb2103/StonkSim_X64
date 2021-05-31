import mysql.connector as sql
import mysql.connector.errors as Error

isConnected = False

con = None
sqlCur = None

table = None

createTableCommand = '''create table IF NOT EXISTS companyData
                (S_Ticker varchar(15),
                S_Company varchar(60) primary key,
                S_CurrentPrice varchar(10),
                S_Change varchar(10),
                S_ChangeP varchar(10),
                S_Open varchar(10),
                S_PreviousClose varchar(10));'''

class sqlFunctions():
    
    ## INITIALIZES CONNECTION
    def initCon(self):
        global con
        global isConnected
        con = sql.connect(user="root", host="localhost", passwd="password")

        #debug
        try:
            if(con.is_connected()):
                print("Connected")
                isConnected = True
        except Exception as e:
            print(e)
    
    ## CHECKS FOR DATABASE
    def checkForDB(self):
        global sqlCur
        if(isConnected):
            if(con != None):
                sqlCur = con.cursor()
                sqlCur.execute("create database IF NOT EXISTS StonkSim;")
        else:
            print("Connection Doesnt Exist")

    ## CHECKS FOR TABLE
    def checkForTB(self):
        global con
        if(isConnected):
            if(con != None):
                global sqlCur
                con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
                sqlCur = con.cursor()
                sqlCur.execute(createTableCommand)
                
        else:
            print("Connection Doesnt Exist")
    
    def getTableData(self):
        from ui_functions import UIFunctions
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
        cmd = "select * from companydata;"
        sqlCur.execute(cmd)
        table = sqlCur.fetchall()
        print(table)
        UIFunctions.refreshUItable(self, table)

    ## INITIALIZES THE SQL DATABASE FOR READ-WRITE--ABILITY
    def initSQL(self):
        sqlFunctions.initCon(self)
        sqlFunctions.checkForDB(self)
        sqlFunctions.checkForTB(self)