from main import *
from stock_functions import *
from sql_functions import *
import time

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
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        
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
        self.ui.tableWidget.setRowCount(3)
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

        if(SEARCH_STATE == 1):
            ticker = stockFunctions.returnTickerSymbol(self, cursorQuery)
            print(cursorQuery, ticker, "searchstate:" + str(SEARCH_STATE))
            try:
                stockFunctions.returnCompanyDetails2(self, ticker, cursorQuery)
            except Error as e:
                print(e)
        elif(SEARCH_STATE == 0):
            print(cursorQuery, "searchstate:" + str(SEARCH_STATE))
            try:
                stockFunctions.returnCompanyDetails2(self, cursorQuery, cursorQuery)
            except Error as e:
                print(e)
        
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