import sys
import subprocess
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

terminateThread = False
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

        ## INITIALIZE THE JSON
        JSONFuntions.createJSON(self)
        threadProcess = subprocess.Popen(["python", "main_thread.py"])
        if(terminateThread):
            threadProcess.terminate()

        ## TOGGLE/BURGER MENU
        ########################################################################
        self.ui.expand_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 120, True))

        ## PAGES
        ########################################################################
        UIFunctions.setPage1(self);
        
        # Page Init
        # PAGE 1
        
        self.ui.Page_btn_1.clicked.connect(lambda: UIFunctions.setPage1(self))
        self.ui.addToTable_pushButton.clicked.connect(lambda: UIFunctions.onAddCompanyButtonClick(self))
        self.ui.InputType_checkBox.stateChanged.connect(lambda: UIFunctions.setSearchStateCheckboxText(self))
        
        # PAGE 2
        self.ui.Page_btn_2.clicked.connect(lambda: UIFunctions.setPage2(self))
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())