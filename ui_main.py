# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testBseced.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 645)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 51))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.expand_frame = QFrame(self.top_bar)
        self.expand_frame.setObjectName(u"expand_frame")
        self.expand_frame.setMaximumSize(QSize(70, 16777215))
        self.expand_frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: 0px solid")
        self.expand_frame.setFrameShape(QFrame.StyledPanel)
        self.expand_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.expand_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.expand_btn = QPushButton(self.expand_frame)
        self.expand_btn.setObjectName(u"expand_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expand_btn.sizePolicy().hasHeightForWidth())
        self.expand_btn.setSizePolicy(sizePolicy)
        self.expand_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}r")
        icon = QIcon()
        icon.addFile(u"Resources/icons8-menu-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_btn.setIcon(icon)
        self.expand_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.expand_btn)


        self.horizontalLayout_2.addWidget(self.expand_frame)

        self.titlebar_frame = QFrame(self.top_bar)
        self.titlebar_frame.setObjectName(u"titlebar_frame")
        self.titlebar_frame.setFrameShape(QFrame.NoFrame)
        self.titlebar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titlebar_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimizeBtn = QPushButton(self.titlebar_frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"Resources/icons8-minimize-window-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon1)
        self.minimizeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.titlebar_frame)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Resources/icons8-maximize-button-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon2)
        self.maximizeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.titlebar_frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 79, 79);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Resources/icons8-multiply-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.titlebar_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.top_bar)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_frame = QFrame(self.content_frame)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMinimumSize(QSize(70, 0))
        self.button_frame.setMaximumSize(QSize(70, 16777215))
        self.button_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.button_frame.setFrameShape(QFrame.NoFrame)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.button_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonHolder_Frame = QFrame(self.button_frame)
        self.buttonHolder_Frame.setObjectName(u"buttonHolder_Frame")
        self.buttonHolder_Frame.setFrameShape(QFrame.NoFrame)
        self.buttonHolder_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttonHolder_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Page_btn_1 = QPushButton(self.buttonHolder_Frame)
        self.Page_btn_1.setObjectName(u"Page_btn_1")
        self.Page_btn_1.setMinimumSize(QSize(0, 60))
        self.Page_btn_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}r")
        icon4 = QIcon()
        icon4.addFile(u"Resources/icons8-table-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Page_btn_1.setIcon(icon4)
        self.Page_btn_1.setIconSize(QSize(24, 24))
        self.Page_btn_1.setCheckable(False)

        self.verticalLayout_3.addWidget(self.Page_btn_1)

        self.Page_btn_2 = QPushButton(self.buttonHolder_Frame)
        self.Page_btn_2.setObjectName(u"Page_btn_2")
        self.Page_btn_2.setMinimumSize(QSize(0, 60))
        self.Page_btn_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}r")
        icon5 = QIcon()
        icon5.addFile(u"Resources/icons8-graph-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Page_btn_2.setIcon(icon5)
        self.Page_btn_2.setIconSize(QSize(24, 24))
        self.Page_btn_2.setCheckable(False)

        self.verticalLayout_3.addWidget(self.Page_btn_2)

        self.Page_btn_3 = QPushButton(self.buttonHolder_Frame)
        self.Page_btn_3.setObjectName(u"Page_btn_3")
        self.Page_btn_3.setMinimumSize(QSize(0, 60))
        self.Page_btn_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}r")
        icon6 = QIcon()
        icon6.addFile(u"Resources/icons8-money-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Page_btn_3.setIcon(icon6)
        self.Page_btn_3.setIconSize(QSize(24, 24))
        self.Page_btn_3.setCheckable(False)

        self.verticalLayout_3.addWidget(self.Page_btn_3)


        self.verticalLayout_2.addWidget(self.buttonHolder_Frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.button_frame)

        self.buttonNames_frame = QFrame(self.content_frame)
        self.buttonNames_frame.setObjectName(u"buttonNames_frame")
        self.buttonNames_frame.setEnabled(True)
        self.buttonNames_frame.setMinimumSize(QSize(0, 0))
        self.buttonNames_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.buttonNames_frame.setFrameShape(QFrame.NoFrame)
        self.buttonNames_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.buttonNames_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnLabelHolder_frame = QFrame(self.buttonNames_frame)
        self.btnLabelHolder_frame.setObjectName(u"btnLabelHolder_frame")
        self.btnLabelHolder_frame.setMinimumSize(QSize(0, 60))
        self.btnLabelHolder_frame.setFrameShape(QFrame.NoFrame)
        self.btnLabelHolder_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.btnLabelHolder_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn1Label_frame = QFrame(self.btnLabelHolder_frame)
        self.btn1Label_frame.setObjectName(u"btn1Label_frame")
        self.btn1Label_frame.setMinimumSize(QSize(0, 60))
        self.btn1Label_frame.setFrameShape(QFrame.NoFrame)
        self.btn1Label_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.btn1Label_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(6, 9, 141, 41))
        font = QFont()
        font.setFamily(u"Roboto Thin")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.btn1Label_frame)

        self.btn2Label_frame = QFrame(self.btnLabelHolder_frame)
        self.btn2Label_frame.setObjectName(u"btn2Label_frame")
        self.btn2Label_frame.setMinimumSize(QSize(0, 60))
        self.btn2Label_frame.setFrameShape(QFrame.NoFrame)
        self.btn2Label_frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.btn2Label_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(6, 9, 141, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.btn2Label_frame)

        self.btn3Label_frame = QFrame(self.btnLabelHolder_frame)
        self.btn3Label_frame.setObjectName(u"btn3Label_frame")
        self.btn3Label_frame.setMinimumSize(QSize(0, 60))
        self.btn3Label_frame.setFrameShape(QFrame.NoFrame)
        self.btn3Label_frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.btn3Label_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(6, 2, 141, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.btn3Label_frame)


        self.verticalLayout_5.addWidget(self.btnLabelHolder_frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.buttonNames_frame)

        self.content_area = QFrame(self.content_frame)
        self.content_area.setObjectName(u"content_area")
        self.content_area.setFrameShape(QFrame.NoFrame)
        self.content_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_area)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_area)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.table_page = QWidget()
        self.table_page.setObjectName(u"table_page")
        self.verticalLayout_8 = QVBoxLayout(self.table_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(60, 30, 60, 30)
        self.Search_parent = QFrame(self.table_page)
        self.Search_parent.setObjectName(u"Search_parent")
        self.Search_parent.setMinimumSize(QSize(450, 50))
        self.Search_parent.setMaximumSize(QSize(390, 50))
        self.Search_parent.setFrameShape(QFrame.NoFrame)
        self.Search_parent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Search_parent)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.companyInput_lineEdit = QLineEdit(self.Search_parent)
        self.companyInput_lineEdit.setObjectName(u"companyInput_lineEdit")
        self.companyInput_lineEdit.setMinimumSize(QSize(320, 45))
        self.companyInput_lineEdit.setMaximumSize(QSize(380, 45))
        self.companyInput_lineEdit.setFont(font)
        self.companyInput_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.companyInput_lineEdit.setMaxLength(20)
        self.companyInput_lineEdit.setCursorPosition(0)
        self.companyInput_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.horizontalLayout_7.addWidget(self.companyInput_lineEdit)

        self.addToTable_pushButton = QPushButton(self.Search_parent)
        self.addToTable_pushButton.setObjectName(u"addToTable_pushButton")
        self.addToTable_pushButton.setMinimumSize(QSize(45, 45))
        self.addToTable_pushButton.setMaximumSize(QSize(45, 45))
        self.addToTable_pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 22px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"Resources/icons8-plus-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addToTable_pushButton.setIcon(icon7)
        self.addToTable_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.addToTable_pushButton)


        self.verticalLayout_8.addWidget(self.Search_parent, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer)

        self.tableWidget = QTableWidget(self.table_page)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setStyleSheet(u"QTableView{\n"
"background-color: rgb(35, 35, 35);\n"
"border: 0px;\n"
"border-radius: 9px;\n"
"}\n"
"QHeaderView::section{\n"
"	color: #FFFFFF;\n"
"	background-color: rgb(30, 30, 30);\n"
"	height: 30px;\n"
"	border: 0px solid;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.table_page)
        self.graphs_page = QWidget()
        self.graphs_page.setObjectName(u"graphs_page")
        self.verticalLayout_9 = QVBoxLayout(self.graphs_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.graphs_page)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(24)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.graphs_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.verticalLayout_7 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.accounts_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.accounts_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.bottom_frame = QFrame(self.content_area)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 20))
        self.bottom_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.bottom_frame.setLineWidth(1)
        self.horizontalLayout_5 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.DebugText = QLabel(self.bottom_frame)
        self.DebugText.setObjectName(u"DebugText")
        font2 = QFont()
        font2.setFamily(u"Roboto Light")
        font2.setPointSize(10)
        self.DebugText.setFont(font2)
        self.DebugText.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.DebugText)

        self.bottom_framechild = QFrame(self.bottom_frame)
        self.bottom_framechild.setObjectName(u"bottom_framechild")
        self.bottom_framechild.setFrameShape(QFrame.NoFrame)
        self.bottom_framechild.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottom_framechild)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.resize_grip_frame = QFrame(self.bottom_framechild)
        self.resize_grip_frame.setObjectName(u"resize_grip_frame")
        self.resize_grip_frame.setMinimumSize(QSize(20, 0))
        self.resize_grip_frame.setStyleSheet(u"background-color: rgb(135, 135, 135);")
        self.resize_grip_frame.setFrameShape(QFrame.StyledPanel)
        self.resize_grip_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.resize_grip_frame)


        self.horizontalLayout_5.addWidget(self.bottom_framechild, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.bottom_frame, 0, Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.content_area)


        self.verticalLayout.addWidget(self.content_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test", None))
        self.expand_btn.setText("")
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.Page_btn_1.setText("")
        self.Page_btn_2.setText("")
        self.Page_btn_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.companyInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.addToTable_pushButton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Current Price", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Change", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Change %", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Open", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Previous Close", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.DebugText.setText("")
    # retranslateUi

