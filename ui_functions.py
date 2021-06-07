import requests
from PySide2 import QtCore
import random
import multiprocessing

from main import *
from json_functions import *
from graph_functions import *

GLOBAL_STATE = 0
SEARCH_STATE = 0

# DEBUG LINE STYLESHEETS
debugRed = u"color: rgb(255, 84, 84);"
debugGreen = u"color: rgb(126, 255, 90);"

# BUTTON STYLESHEET STATES
btnSelected = u"""
QPushButton{
	color: rgb(255, 255, 255);
	background-color: rgb(45, 45, 45);
	border: 0px solid;
}
QPushButton:hover {
	background-color: rgb(85, 170, 255);
}
"""

btnUnSelected = u"""
QPushButton{
	color: rgb(255, 255, 255);
	background-color: rgb(35, 35, 35);
	border: 0px solid;
}
QPushButton:hover {
	background-color: rgb(85, 170, 255);
}
"""

btnLabelFrameSelected = u"""
background-color: rgb(45, 45, 45);
"""

btnLabelFrameUnSelected = u"""
background-color: rgb(35, 35, 35);
"""

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            #get the width
            width = self.ui.buttonNames_frame.width()
            maxExtend = maxWidth
            standard = 0

            #set the max width
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #anim
            self.animation = QPropertyAnimation(self.ui.buttonNames_frame, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def UIDefs(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## TITLEBAR BUTTONS
        self.ui.closeBtn.setToolTip("Close")
        self.ui.closeBtn.clicked.connect(lambda: UIFunctions.closeProgram(self))
        
        self.ui.maximizeBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        
        self.ui.minimizeBtn.setToolTip("Minimize")
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())

        ## SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.resize_grip_frame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

        ## RESIZE TABLE COLUMN HEADERS EQUALLY
        tableHeader = self.ui.tableWidget.horizontalHeader()
        tableHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        ## HIDE VERTICAL HEADER AND ALSO ADD NUMBER OF ROWS (FOR REFERENCE)
        #self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.verticalHeader().hide()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            self.ui.maximizeBtn.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.maximizeBtn.setToolTip("Maximize")
    
    def setPage1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.table_page)
        self.ui.Page_btn_1.setStyleSheet(btnSelected)
        self.ui.Page_btn_2.setStyleSheet(btnUnSelected)
        self.ui.Page_btn_3.setStyleSheet(btnUnSelected)
        self.ui.btn1Label_frame.setStyleSheet(btnLabelFrameSelected)
        self.ui.btn2Label_frame.setStyleSheet(btnLabelFrameUnSelected)
        self.ui.btn3Label_frame.setStyleSheet(btnLabelFrameUnSelected)

    def setPage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.graphs_page)
        self.ui.Page_btn_1.setStyleSheet(btnUnSelected)
        self.ui.Page_btn_2.setStyleSheet(btnSelected)
        self.ui.Page_btn_3.setStyleSheet(btnUnSelected)
        self.ui.btn1Label_frame.setStyleSheet(btnLabelFrameUnSelected)
        self.ui.btn2Label_frame.setStyleSheet(btnLabelFrameSelected)
        self.ui.btn3Label_frame.setStyleSheet(btnLabelFrameUnSelected)

    def setPage3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page)
        self.ui.Page_btn_1.setStyleSheet(btnUnSelected)
        self.ui.Page_btn_2.setStyleSheet(btnUnSelected)
        self.ui.Page_btn_3.setStyleSheet(btnSelected)
        self.ui.btn1Label_frame.setStyleSheet(btnLabelFrameUnSelected)
        self.ui.btn2Label_frame.setStyleSheet(btnLabelFrameUnSelected)
        self.ui.btn3Label_frame.setStyleSheet(btnLabelFrameSelected)

    def returnWindowState(self):
        return GLOBAL_STATE

    def onAddCompanyButtonClick(self):
        cursorQuery = self.ui.companyInput_lineEdit.text()
        if(cursorQuery != ""):
            if(SEARCH_STATE == 1):
                JSONFuntions.writeToCompanyList(self, cursorQuery, "lol123", True)
            elif(SEARCH_STATE == 0):
                JSONFuntions.writeToCompanyList(self, "lol123" + str(random.getrandbits(128)), cursorQuery, True)
        self.ui.companyInput_lineEdit.setText("")

    def setSearchStateCheckboxText(self):
        global SEARCH_STATE
        if(self.ui.InputType_checkBox.checkState()):
            self.ui.InputType_checkBox.setText("Search by: Name")
            SEARCH_STATE = 1
        else:
            self.ui.InputType_checkBox.setText("Search by: Ticker")
            SEARCH_STATE = 0

    def setDebugLine(self, content, style):
        self.ui.DebugText.setStyleSheet(style)
        self.ui.DebugText.setText("Debug: " + str(content))
    
    def refreshUItable(self, table):
        self.ui.tableWidget.setRowCount(len(list(table)))
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.resizeRowToContents(row)
            for column in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem(table[row][column + 1]))
                self.ui.tableWidget.item(row, column).setTextAlignment(Qt.AlignHCenter)
                currentItem = self.ui.tableWidget.item(row, column).text()
                if((column == 2 or column == 3) and (currentItem != "")):
                    if("-" in currentItem):
                        ## set text to red
                        self.ui.tableWidget.item(row, column).setBackground(QBrush(QColor(100, 0, 0)))
                    else:
                        ## set text to red
                        self.ui.tableWidget.item(row, column).setBackground(QBrush(QColor(0, 100, 0)))
        QtCore.QTimer.singleShot(100, lambda: UIFunctions.refreshUItable(self, sqlFunctions.getTableData(self)))

    def getSelectedRows(self):
        rows = []
        for idx in self.ui.tableWidget.selectedIndexes():
            rows.append(idx.row())
        return(rows)
    
    ##########################################################################################
    ##Graph Functions

    def refreshGraphDropdown(self):
        GraphFunctions.initDB(GraphFunctions)
        companyDict = GraphFunctions.getCompanyList(GraphFunctions)
        companyList = dict(companyDict).keys()
        comboboxList = [self.ui.Company_combobox.itemText(i) for i in range(self.ui.Company_combobox.count())]

        ##Checks the combobox list for items from the retrieved sql database company list 
        ##and adds attems accordingly
        for i in companyList:
            if(not(i in comboboxList)):
                self.ui.Company_combobox.addItem(i)
        
        ##Checks the retrieved items list for any missing vales from combobox and removes 
        ##the ones missing in the sql database companylist from the combobox
        loopItem = 0
        for i in comboboxList:
            if(not(i in companyList)):
                self.ui.Company_combobox.removeItem(loopItem)
            loopItem += 1
        GraphFunctions.dataLine.setData(GraphFunctions.xData, GraphFunctions.yData)
        QtCore.QTimer.singleShot(1000, lambda: UIFunctions.refreshGraphDropdown(self))
    
    def plotGraph(self):
        companyDict = GraphFunctions.getCompanyList(GraphFunctions)
        GraphFunctions.toSearchCursor = companyDict[self.ui.Company_combobox.currentText()]
        GraphFunctions.searchType = self.ui.timeframe_combobox.currentIndex()

    def closeProgram(self):
        JSONFuntions.deleteJson(self)
        terminatedDBThread = True
        GraphFunctions.killDataFetcherThread = True
        self.close()