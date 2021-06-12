import sys
import mysql.connector as sql
import mysql.connector.errors as Error
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from json_functions import *
from sql_functions import *
from graph_functions import *

canRefresh = False

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##CHECK FOR LEFT CLICK TO MOVE TITLE BAR
        def moveWindow(event):
            if(UIFunctions.returnWindowState(self) == 1):
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()
                event.accept()

        self.ui.top_bar.mouseMoveEvent = moveWindow

        UIFunctions.UIDefs(self)

        ## MYSQL CONNECTION
        sqlFunctions.initSQL(self)

        ## TOGGLE/BURGER MENU
        ########################################################################
        self.ui.expand_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 120, True))

        ## PAGES
        ########################################################################
        
        # Page Init
        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)

        # START PAGE
        self.ui.copyToClipBoard_button.clicked.connect(lambda: UIFunctions.copyGitLinkToClipboard(self))
        self.ui.copyToClipBoard_button_2.clicked.connect(lambda: UIFunctions.copyGitLinkToClipboard(self))
        self.ui.signup_button.clicked.connect(lambda: UIFunctions.signUpButtonClick(self))
        self.ui.login_button.clicked.connect(lambda: UIFunctions.loginButtonClick(self))
        self.ui.createAccount_button.clicked.connect(lambda: UIFunctions.createAccountButtonClick(self))
        self.ui.backToStartpage_button.clicked.connect(lambda: UIFunctions.backToStartPageButtonClick(self))
        self.ui.logout_button.clicked.connect(lambda: UIFunctions.logoutUser(self))

        # PAGE 1
        self.ui.Page_btn_1.clicked.connect(lambda: UIFunctions.setPage1(self))
        self.ui.addToTable_pushButton.clicked.connect(lambda: UIFunctions.onAddCompanyButtonClick(self))
        self.ui.InputType_checkBox.stateChanged.connect(lambda: UIFunctions.setSearchStateCheckboxText(self))
        
        # PAGE 2
        self.ui.Page_btn_2.clicked.connect(lambda: UIFunctions.setPage2(self))
        self.ui.Company_combobox.activated.connect(lambda: UIFunctions.plotGraph(self))
        self.ui.timeframe_combobox.activated.connect(lambda: UIFunctions.plotGraph(self))
        
        # PAGE 3
        self.ui.Page_btn_3.clicked.connect(lambda: UIFunctions.setPage3(self))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        ## ==> END ##

    ##APP EVENTS
    #######################################################################

    def mousePressEvent(self, event):
        self.dragpos = event.globalPos()
    
    def keyPressEvent(self, event):
        ## Delete key
        if(event.key() == 16777223):
            try:
                row = UIFunctions.getSelectedRows(self)[0]
                JSONFuntions.writeToCompanyList(self, self.ui.tableWidget.item(row, 0).text(), "ticker", False)
            except IndexError:
                print("No record selected")

        ## Escape Key
        if(event.key() == 16777216):
            self.ui.tableWidget.clearSelection()
            try:
                QApplication.focusWidget().clearFocus()
            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())