import mysql.connector as sql
import mysql.connector.errors as Error

from json_functions import *

isConnected = False

con = None
sqlCur = None

currentTable = ""

createUserPassTableCommand = '''create table IF NOT EXISTS logindata
                (L_Username varchar(50) primary key,
                L_Password varchar(50),
                L_Email varchar(50));'''

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
                sqlCur.execute(createUserPassTableCommand)
        else:
            print("Connection Doesnt Exist")
    
    def getTableData(self, tableName):
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
        cmd = f"select * from {tableName};"
        sqlCur.execute(cmd)
        table = sqlCur.fetchall()
        return table
    
    def createUser(self, username, password, email):
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
        username2 = str(username).rstrip(" ")
        username2 = username2.lstrip(" ")
        username2 = username2.replace(" ", "_")
        try:
            cmd = "INSERT INTO logindata (L_Username, L_Password, L_Email) VALUES(%s,%s,%s)"
            sqlCur.execute(cmd, (username2, password, email))
            con.commit()
        except Error.IntegrityError:
            print(f"User with username {username2} already exists")
            return False
        else:
            cmd = '''create table IF NOT EXISTS ''' + (username2 + "_table") + '''
                    (S_Ticker varchar(15),
                    S_Company varchar(60) primary key,
                    S_CurrentPrice varchar(10),
                    S_Change varchar(10),
                    S_ChangeP varchar(10),
                    S_Open varchar(10),
                    S_PreviousClose varchar(10));'''
            sqlCur.execute(cmd)
            return True
    
    def checkLoginData(self, username, password):
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
        cmd = "show tables;"
        sqlCur.execute(cmd)
        tableList = sqlCur.fetchall()
        username2 = str(username).replace(" ", "_")
        for i in tableList:
            if(i[0][0:-6] == username2):
                cmd = "SELECT * FROM logindata;"
                sqlCur.execute(cmd)
                userList = sqlCur.fetchall()
                for j in userList:
                    if((j[0] == username2) and j[1] == password):
                        global currentTable
                        currentTable = (str(username2) + "_table")
                        JSONFuntions.createTableTextFile(JSONFuntions, (str(username2) + "_table"))
                        return True
        return False
    
    def checkUserExist(self, UserName):
        con = sql.connect(user="root", host="localhost", passwd="password", db="stonksim")
        sqlCur = con.cursor()
        cmd = "show tables;"
        sqlCur.execute(cmd)
        username2 = str(UserName).rstrip(" ")
        username2 = username2.lstrip(" ")
        username2 = username2.replace(" ", "_")
        tableList = sqlCur.fetchall()
        for i in tableList:
            if(i[0][0:-6] == username2):
                exist = True
                print(username2)
                return True
        return False
    
    def getCurrentTable(self):
        global currentTable
        return currentTable

    ## INITIALIZES THE SQL DATABASE FOR READ-WRITE--ABILITY
    def initSQL(self):
        sqlFunctions.initCon(self)
        sqlFunctions.checkForDB(self)
        sqlFunctions.checkForTB(self)
    