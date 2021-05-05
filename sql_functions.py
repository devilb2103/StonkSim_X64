import mysql.connector as sql
import mysql.connector.errors as Error
from main import MainWindow

isConnected = False

con = None
sqlCur = None

createTableCommand = '''create table IF NOT EXISTS companyData
                (S_Company char(40) primary key,
                S_CurrentPrice char(10),
                S_Change char(10),
                S_ChangeP char(10),
                S_Open char(10),
                S_PreviousClose char(10));'''

class sqlFunctions(MainWindow):

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
                con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
                sqlCur = con.cursor()
                sqlCur.execute(createTableCommand)
                
        else:
            print("Connection Doesnt Exist")
    
    ## INITIALIZES THE SQL DATABASE FOR READ-WRITE--ABILITY
    def initSQL(self):
        sqlFunctions.initCon(self)
        sqlFunctions.checkForDB(self)
        sqlFunctions.checkForTB(self)