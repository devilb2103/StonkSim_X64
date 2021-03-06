# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testNUNGCB.ui'
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

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 660)
        MainWindow.setMinimumSize(QSize(1000, 660))
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
        self.expand_frame.setMaximumSize(QSize(0, 16777215))
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
"	outline: 0;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
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
"	border: 0px solid;\n"
"	outline: 0;\n"
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
"	border: 0px solid;\n"
"	outline: 0;\n"
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
"	border: 0px solid;\n"
"	outline: 0;\n"
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
        self.buttonHolder_Frame.setMaximumSize(QSize(0, 16777215))
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
"}\n"
"QPushButton:focus {\n"
"	border: none;\n"
"	outline: none;\n"
"	padding: -1;\n"
"}")
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
"}\n"
"QPushButton:focus {\n"
"	border: none;\n"
"	outline: none;\n"
"	padding: -1;\n"
"}")
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
"}\n"
"QPushButton:focus {\n"
"	border: none;\n"
"	outline: none;\n"
"	padding: -1;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"Resources/icons8-money-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Page_btn_3.setIcon(icon6)
        self.Page_btn_3.setIconSize(QSize(24, 24))
        self.Page_btn_3.setCheckable(False)

        self.verticalLayout_3.addWidget(self.Page_btn_3)


        self.verticalLayout_2.addWidget(self.buttonHolder_Frame)

        self.verticalSpacer_10 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.logoutButtonContainer = QFrame(self.button_frame)
        self.logoutButtonContainer.setObjectName(u"logoutButtonContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoutButtonContainer.sizePolicy().hasHeightForWidth())
        self.logoutButtonContainer.setSizePolicy(sizePolicy1)
        self.logoutButtonContainer.setMinimumSize(QSize(0, 60))
        self.logoutButtonContainer.setMaximumSize(QSize(0, 16777215))
        self.logoutButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.logoutButtonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.logoutButtonContainer)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.logout_button = QPushButton(self.logoutButtonContainer)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMinimumSize(QSize(45, 45))
        self.logout_button.setMaximumSize(QSize(45, 45))
        self.logout_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 79, 79);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(235, 59, 59);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"Resources/icons8-logout-rounded-left-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_button.setIcon(icon7)
        self.logout_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.logout_button)


        self.verticalLayout_2.addWidget(self.logoutButtonContainer)


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
        self.stackedWidget.setStyleSheet(u"")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.start_page.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout_10 = QVBoxLayout(self.start_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 70, 21)
        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.title_label = QLabel(self.start_page)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(48)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.username_lineEdit = QLineEdit(self.start_page)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setMinimumSize(QSize(320, 45))
        self.username_lineEdit.setMaximumSize(QSize(360, 45))
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_10.addWidget(self.username_lineEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.Password_lineEdit = QLineEdit(self.start_page)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setMinimumSize(QSize(320, 45))
        self.Password_lineEdit.setMaximumSize(QSize(360, 45))
        self.Password_lineEdit.setFont(font)
        self.Password_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")
        self.Password_lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.Password_lineEdit, 0, Qt.AlignHCenter)

        self.forgotPassword_button = QPushButton(self.start_page)
        self.forgotPassword_button.setObjectName(u"forgotPassword_button")
        font2 = QFont()
        font2.setFamily(u"Roboto Thin")
        font2.setPointSize(10)
        self.forgotPassword_button.setFont(font2)
        self.forgotPassword_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"	padding-top: 9px;\n"
"}")

        self.verticalLayout_10.addWidget(self.forgotPassword_button, 0, Qt.AlignHCenter)

        self.loginsignup_container = QFrame(self.start_page)
        self.loginsignup_container.setObjectName(u"loginsignup_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginsignup_container.sizePolicy().hasHeightForWidth())
        self.loginsignup_container.setSizePolicy(sizePolicy2)
        self.loginsignup_container.setMinimumSize(QSize(300, 50))
        self.loginsignup_container.setMaximumSize(QSize(0, 0))
        self.loginsignup_container.setFrameShape(QFrame.NoFrame)
        self.loginsignup_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.loginsignup_container)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.login_button = QPushButton(self.loginsignup_container)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(120, 39))
        self.login_button.setMaximumSize(QSize(120, 39))
        self.login_button.setFont(font)
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}")

        self.horizontalLayout_15.addWidget(self.login_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.signup_button = QPushButton(self.loginsignup_container)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setMinimumSize(QSize(120, 39))
        self.signup_button.setMaximumSize(QSize(120, 39))
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}")

        self.horizontalLayout_15.addWidget(self.signup_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.loginsignup_container, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.link_container = QFrame(self.start_page)
        self.link_container.setObjectName(u"link_container")
        self.link_container.setMinimumSize(QSize(0, 0))
        self.link_container.setStyleSheet(u"border-radius: 15;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left: 12px;\n"
"padding-right: 12px;\n"
"padding-top: 6px;\n"
"padding-bottom: 6px;")
        self.link_container.setFrameShape(QFrame.NoFrame)
        self.link_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.link_container)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.github_label = QLabel(self.link_container)
        self.github_label.setObjectName(u"github_label")
        font3 = QFont()
        font3.setFamily(u"Roboto Thin")
        font3.setPointSize(24)
        self.github_label.setFont(font3)
        self.github_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(35, 35, 35);\n"
"")
        self.github_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.github_label)

        self.copyToClipBoard_button = QPushButton(self.link_container)
        self.copyToClipBoard_button.setObjectName(u"copyToClipBoard_button")
        self.copyToClipBoard_button.setMinimumSize(QSize(45, 45))
        self.copyToClipBoard_button.setMaximumSize(QSize(45, 45))
        self.copyToClipBoard_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"Resources/icons8-copy-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyToClipBoard_button.setIcon(icon8)
        self.copyToClipBoard_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.copyToClipBoard_button)


        self.verticalLayout_10.addWidget(self.link_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.start_page)
        self.email_page = QWidget()
        self.email_page.setObjectName(u"email_page")
        self.email_page.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout_11 = QVBoxLayout(self.email_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 70, 21)
        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.title_label_2 = QLabel(self.email_page)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setFont(font1)
        self.title_label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.title_label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.email_lineEdit = QLineEdit(self.email_page)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(390, 45))
        self.email_lineEdit.setMaximumSize(QSize(390, 45))
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_11.addWidget(self.email_lineEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.createAccount_button = QPushButton(self.email_page)
        self.createAccount_button.setObjectName(u"createAccount_button")
        self.createAccount_button.setMinimumSize(QSize(210, 39))
        self.createAccount_button.setMaximumSize(QSize(210, 39))
        self.createAccount_button.setFont(font)
        self.createAccount_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_11.addWidget(self.createAccount_button, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_9)

        self.backToStartpage_button = QPushButton(self.email_page)
        self.backToStartpage_button.setObjectName(u"backToStartpage_button")
        self.backToStartpage_button.setMinimumSize(QSize(45, 45))
        self.backToStartpage_button.setMaximumSize(QSize(45, 45))
        self.backToStartpage_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"Resources/icons8-double-left-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backToStartpage_button.setIcon(icon9)
        self.backToStartpage_button.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.backToStartpage_button, 0, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 212, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_8)

        self.link_container_2 = QFrame(self.email_page)
        self.link_container_2.setObjectName(u"link_container_2")
        self.link_container_2.setStyleSheet(u"border-radius: 15;\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left: 12px;\n"
"padding-right: 12px;\n"
"padding-top: 6px;\n"
"padding-bottom: 6px;")
        self.link_container_2.setFrameShape(QFrame.NoFrame)
        self.link_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.link_container_2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.github_label_2 = QLabel(self.link_container_2)
        self.github_label_2.setObjectName(u"github_label_2")
        self.github_label_2.setFont(font3)
        self.github_label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(35, 35, 35);\n"
"")
        self.github_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.github_label_2)

        self.copyToClipBoard_button_2 = QPushButton(self.link_container_2)
        self.copyToClipBoard_button_2.setObjectName(u"copyToClipBoard_button_2")
        self.copyToClipBoard_button_2.setMinimumSize(QSize(45, 45))
        self.copyToClipBoard_button_2.setMaximumSize(QSize(45, 45))
        self.copyToClipBoard_button_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"")
        self.copyToClipBoard_button_2.setIcon(icon8)
        self.copyToClipBoard_button_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.copyToClipBoard_button_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.link_container_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.email_page)
        self.forgotPassword_page = QWidget()
        self.forgotPassword_page.setObjectName(u"forgotPassword_page")
        self.forgotPassword_page.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout_12 = QVBoxLayout(self.forgotPassword_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 70, 21)
        self.verticalSpacer_11 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)

        self.title_label_3 = QLabel(self.forgotPassword_page)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setFont(font1)
        self.title_label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.title_label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.forgotUsername_lineEdit = QLineEdit(self.forgotPassword_page)
        self.forgotUsername_lineEdit.setObjectName(u"forgotUsername_lineEdit")
        self.forgotUsername_lineEdit.setMinimumSize(QSize(320, 45))
        self.forgotUsername_lineEdit.setMaximumSize(QSize(320, 45))
        self.forgotUsername_lineEdit.setFont(font)
        self.forgotUsername_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_12.addWidget(self.forgotUsername_lineEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_13)

        self.forgotEmail_lineEdit = QLineEdit(self.forgotPassword_page)
        self.forgotEmail_lineEdit.setObjectName(u"forgotEmail_lineEdit")
        self.forgotEmail_lineEdit.setMinimumSize(QSize(320, 45))
        self.forgotEmail_lineEdit.setMaximumSize(QSize(390, 45))
        self.forgotEmail_lineEdit.setFont(font)
        self.forgotEmail_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_12.addWidget(self.forgotEmail_lineEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_14)

        self.sendVerificationCodeContainer = QFrame(self.forgotPassword_page)
        self.sendVerificationCodeContainer.setObjectName(u"sendVerificationCodeContainer")
        self.sendVerificationCodeContainer.setMinimumSize(QSize(0, 0))
        self.sendVerificationCodeContainer.setFrameShape(QFrame.StyledPanel)
        self.sendVerificationCodeContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.sendVerificationCodeContainer)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.backToStartpage_button_2 = QPushButton(self.sendVerificationCodeContainer)
        self.backToStartpage_button_2.setObjectName(u"backToStartpage_button_2")
        self.backToStartpage_button_2.setMinimumSize(QSize(45, 45))
        self.backToStartpage_button_2.setMaximumSize(QSize(45, 45))
        self.backToStartpage_button_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"")
        self.backToStartpage_button_2.setIcon(icon9)
        self.backToStartpage_button_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.backToStartpage_button_2)

        self.sendVerificationCode_button = QPushButton(self.sendVerificationCodeContainer)
        self.sendVerificationCode_button.setObjectName(u"sendVerificationCode_button")
        self.sendVerificationCode_button.setMinimumSize(QSize(270, 39))
        self.sendVerificationCode_button.setMaximumSize(QSize(270, 39))
        self.sendVerificationCode_button.setFont(font)
        self.sendVerificationCode_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}")

        self.horizontalLayout_18.addWidget(self.sendVerificationCode_button)


        self.verticalLayout_12.addWidget(self.sendVerificationCodeContainer, 0, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_15)

        self.newPasswordContainer = QFrame(self.forgotPassword_page)
        self.newPasswordContainer.setObjectName(u"newPasswordContainer")
        self.newPasswordContainer.setMaximumSize(QSize(16777215, 150))
        self.newPasswordContainer.setFrameShape(QFrame.StyledPanel)
        self.newPasswordContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.newPasswordContainer)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verificationCode_lineEdit = QLineEdit(self.newPasswordContainer)
        self.verificationCode_lineEdit.setObjectName(u"verificationCode_lineEdit")
        self.verificationCode_lineEdit.setMinimumSize(QSize(320, 45))
        self.verificationCode_lineEdit.setMaximumSize(QSize(320, 45))
        self.verificationCode_lineEdit.setFont(font)
        self.verificationCode_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")
        self.verificationCode_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.verificationCode_lineEdit, 0, Qt.AlignHCenter)

        self.newPassword_lineEdit = QLineEdit(self.newPasswordContainer)
        self.newPassword_lineEdit.setObjectName(u"newPassword_lineEdit")
        self.newPassword_lineEdit.setMinimumSize(QSize(320, 45))
        self.newPassword_lineEdit.setMaximumSize(QSize(320, 45))
        self.newPassword_lineEdit.setFont(font)
        self.newPassword_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_13.addWidget(self.newPassword_lineEdit, 0, Qt.AlignHCenter)

        self.changePassword_button = QPushButton(self.newPasswordContainer)
        self.changePassword_button.setObjectName(u"changePassword_button")
        self.changePassword_button.setMinimumSize(QSize(240, 39))
        self.changePassword_button.setMaximumSize(QSize(240, 39))
        self.changePassword_button.setFont(font)
        self.changePassword_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 0px solid;\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	outline: 0;\n"
"}")

        self.verticalLayout_13.addWidget(self.changePassword_button, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.newPasswordContainer, 0, Qt.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_16)

        self.stackedWidget.addWidget(self.forgotPassword_page)
        self.table_page = QWidget()
        self.table_page.setObjectName(u"table_page")
        self.verticalLayout_8 = QVBoxLayout(self.table_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(60, 30, 60, 30)
        self.Table_page_Topbar = QFrame(self.table_page)
        self.Table_page_Topbar.setObjectName(u"Table_page_Topbar")
        self.Table_page_Topbar.setFrameShape(QFrame.NoFrame)
        self.Table_page_Topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Table_page_Topbar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Search_parent = QFrame(self.Table_page_Topbar)
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
"	padding-left: 12px;\n"
"	outline: 0;\n"
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
"	outline: 0;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 22px;\n"
"	outline: 0;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"Resources/icons8-plus-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addToTable_pushButton.setIcon(icon10)
        self.addToTable_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.addToTable_pushButton)


        self.horizontalLayout_8.addWidget(self.Search_parent)

        self.SwitchSearchType_Parent = QFrame(self.Table_page_Topbar)
        self.SwitchSearchType_Parent.setObjectName(u"SwitchSearchType_Parent")
        font4 = QFont()
        font4.setFamily(u"Roboto Thin")
        self.SwitchSearchType_Parent.setFont(font4)
        self.SwitchSearchType_Parent.setStyleSheet(u"")
        self.SwitchSearchType_Parent.setFrameShape(QFrame.NoFrame)
        self.SwitchSearchType_Parent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.SwitchSearchType_Parent)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, 0, 0, 0)
        self.InputType_checkBox = QCheckBox(self.SwitchSearchType_Parent)
        self.InputType_checkBox.setObjectName(u"InputType_checkBox")
        font5 = QFont()
        font5.setFamily(u"Roboto Thin")
        font5.setPointSize(16)
        self.InputType_checkBox.setFont(font5)
        self.InputType_checkBox.setStyleSheet(u"QCheckBox::indicator:checked\n"
"{\n"
"	border : 2px solid white;\n"
"	width : 20px;\n"
"	height : 20px;\n"
"	border-radius : 12px;\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"QCheckBox::indicator:checked:pressed\n"
"{\n"
"	border : 2px solid white;\n"
"	width : 20px;\n"
"	height : 20px;\n"
"	border-radius : 12px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed\n"
"{\n"
"	border : 2px solid white;\n"
"	width : 20px;\n"
"	height : 20px;\n"
"	border-radius : 12px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"	border : 2px solid white;\n"
"	width : 20px;\n"
"	height : 20px;\n"
"	border-radius : 12px;\n"
"	background-color: rgb(35, 35, 35);\n"
"}\n"
"QCheckBox\n"
"{\n"
"	color:white;\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_9.addWidget(self.InputType_checkBox)


        self.horizontalLayout_8.addWidget(self.SwitchSearchType_Parent, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.SwitchSearchType_Parent.raise_()
        self.Search_parent.raise_()

        self.verticalLayout_8.addWidget(self.Table_page_Topbar, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer)

        self.tableWidget = QTableWidget(self.table_page)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        font6 = QFont()
        font6.setPointSize(11)
        self.tableWidget.setFont(font6)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setStyleSheet(u"QTableView{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px;\n"
"	border-radius: 9px;\n"
"	selection-background-color: rgb(45,45, 45);\n"
"	selection-color: rgb(255, 255, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	color: #FFFFFF;\n"
"	background-color: rgb(30, 30, 30);\n"
"	height: 30px;\n"
"	border: 0px solid;\n"
"}\n"
"QTableView::item {\n"
"	color: #FFFFFF;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.table_page)
        self.graphs_page = QWidget()
        self.graphs_page.setObjectName(u"graphs_page")
        self.verticalLayout_9 = QVBoxLayout(self.graphs_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(60, 30, 60, 30)
        self.Graphs_page_Topbar = QFrame(self.graphs_page)
        self.Graphs_page_Topbar.setObjectName(u"Graphs_page_Topbar")
        self.Graphs_page_Topbar.setFrameShape(QFrame.NoFrame)
        self.Graphs_page_Topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Graphs_page_Topbar)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Company_DropDown_parent = QFrame(self.Graphs_page_Topbar)
        self.Company_DropDown_parent.setObjectName(u"Company_DropDown_parent")
        self.Company_DropDown_parent.setMinimumSize(QSize(350, 50))
        self.Company_DropDown_parent.setMaximumSize(QSize(390, 50))
        self.Company_DropDown_parent.setFrameShape(QFrame.NoFrame)
        self.Company_DropDown_parent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Company_DropDown_parent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Company_combobox = QComboBox(self.Company_DropDown_parent)
        self.Company_combobox.setObjectName(u"Company_combobox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Company_combobox.sizePolicy().hasHeightForWidth())
        self.Company_combobox.setSizePolicy(sizePolicy3)
        self.Company_combobox.setMinimumSize(QSize(320, 45))
        self.Company_combobox.setMaximumSize(QSize(380, 45))
        self.Company_combobox.setFont(font)
        self.Company_combobox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	outline: 0;\n"
"	padding-left: 12px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"	image: none; \n"
"	border-width: 0px;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    border: 0px solid ;\n"
"    color: white;\n"
"    selection-background-color: rgb(35, 35, 35);\n"
"	outline: none;\n"
"	border-radius: 9px;\n"
"}")
        self.Company_combobox.setFrame(True)

        self.horizontalLayout_11.addWidget(self.Company_combobox)


        self.horizontalLayout_10.addWidget(self.Company_DropDown_parent)

        self.timeFrame_dropdown_parent = QFrame(self.Graphs_page_Topbar)
        self.timeFrame_dropdown_parent.setObjectName(u"timeFrame_dropdown_parent")
        self.timeFrame_dropdown_parent.setMinimumSize(QSize(285, 50))
        self.timeFrame_dropdown_parent.setMaximumSize(QSize(285, 50))
        self.timeFrame_dropdown_parent.setFrameShape(QFrame.NoFrame)
        self.timeFrame_dropdown_parent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.timeFrame_dropdown_parent)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.timeframe_combobox = QComboBox(self.timeFrame_dropdown_parent)
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.addItem("")
        self.timeframe_combobox.setObjectName(u"timeframe_combobox")
        sizePolicy3.setHeightForWidth(self.timeframe_combobox.sizePolicy().hasHeightForWidth())
        self.timeframe_combobox.setSizePolicy(sizePolicy3)
        self.timeframe_combobox.setMinimumSize(QSize(270, 45))
        self.timeframe_combobox.setMaximumSize(QSize(270, 45))
        self.timeframe_combobox.setFont(font)
        self.timeframe_combobox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"	outline: 0;\n"
"	padding-left: 12px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"	image: none; \n"
"	border-width: 0px;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    border: 0px solid ;\n"
"    color: white;\n"
"    selection-background-color: rgb(35, 35, 35);\n"
"	outline: none;\n"
"	border-radius: 9px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.timeframe_combobox)


        self.horizontalLayout_10.addWidget(self.timeFrame_dropdown_parent, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.Graphs_page_Topbar, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_2)

        self.graph_container = QFrame(self.graphs_page)
        self.graph_container.setObjectName(u"graph_container")
        sizePolicy.setHeightForWidth(self.graph_container.sizePolicy().hasHeightForWidth())
        self.graph_container.setSizePolicy(sizePolicy)
        self.graph_container.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border: 0px;\n"
"border-radius: 9px;")
        self.graph_container.setFrameShape(QFrame.NoFrame)
        self.graph_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.graph_container)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.graph_widget = PlotWidget(self.graph_container)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.graph_widget.sizePolicy().hasHeightForWidth())
        self.graph_widget.setSizePolicy(sizePolicy)
        self.graph_widget.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border: 0px;\n"
"border-radius: 9px;")

        self.horizontalLayout_13.addWidget(self.graph_widget)


        self.verticalLayout_9.addWidget(self.graph_container)

        self.stackedWidget.addWidget(self.graphs_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.verticalLayout_7 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.accounts_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
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
        self.spacingOffset_frame = QFrame(self.bottom_frame)
        self.spacingOffset_frame.setObjectName(u"spacingOffset_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spacingOffset_frame.sizePolicy().hasHeightForWidth())
        self.spacingOffset_frame.setSizePolicy(sizePolicy4)
        self.spacingOffset_frame.setMinimumSize(QSize(90, 0))
        self.spacingOffset_frame.setFrameShape(QFrame.StyledPanel)
        self.spacingOffset_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.spacingOffset_frame)

        self.DebugText = QLabel(self.bottom_frame)
        self.DebugText.setObjectName(u"DebugText")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.DebugText.sizePolicy().hasHeightForWidth())
        self.DebugText.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setFamily(u"Roboto Light")
        font7.setPointSize(10)
        self.DebugText.setFont(font7)
        self.DebugText.setLayoutDirection(Qt.LeftToRight)
        self.DebugText.setAutoFillBackground(False)
        self.DebugText.setStyleSheet(u"")
        self.DebugText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.DebugText, 0, Qt.AlignRight)

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

        self.stackedWidget.setCurrentIndex(2)


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
        self.logout_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"StonkSim_X64", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.forgotPassword_button.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.signup_button.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.github_label.setText(QCoreApplication.translate("MainWindow", u"https://github.com/devilb2103/StonkSim_X64", None))
        self.copyToClipBoard_button.setText("")
        self.title_label_2.setText(QCoreApplication.translate("MainWindow", u"StonkSim_X64", None))
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.createAccount_button.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.backToStartpage_button.setText("")
        self.github_label_2.setText(QCoreApplication.translate("MainWindow", u"https://github.com/devilb2103/StonkSim_X64", None))
        self.copyToClipBoard_button_2.setText("")
        self.title_label_3.setText(QCoreApplication.translate("MainWindow", u"StonkSim_X64", None))
        self.forgotUsername_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.forgotEmail_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.backToStartpage_button_2.setText("")
        self.sendVerificationCode_button.setText(QCoreApplication.translate("MainWindow", u"Send Verification Code", None))
        self.verificationCode_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Verification Code", None))
        self.newPassword_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.changePassword_button.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.companyInput_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.addToTable_pushButton.setText("")
        self.InputType_checkBox.setText(QCoreApplication.translate("MainWindow", u"Search by: Ticker", None))
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
        self.timeframe_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"This Week", None))
        self.timeframe_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"This Month", None))
        self.timeframe_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Last 6 Months", None))
        self.timeframe_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"This Year", None))
        self.timeframe_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Last 5 Years", None))
        self.timeframe_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"All Time", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.DebugText.setText("")
    # retranslateUi

