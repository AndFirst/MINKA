# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aplication.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1166, 903)
        MainWindow.setMinimumSize(QSize(30, 0))
        MainWindow.setStyleSheet(u"")
        self.users = QAction(MainWindow)
        self.users.setObjectName(u"users")
        self.ranking = QAction(MainWindow)
        self.ranking.setObjectName(u"ranking")
        self.trash_bin = QAction(MainWindow)
        self.trash_bin.setObjectName(u"trash_bin")
        self.throw_trash = QAction(MainWindow)
        self.throw_trash.setObjectName(u"throw_trash")
        self.main = QAction(MainWindow)
        self.main.setObjectName(u"main")
        self.confirm_throwing = QAction(MainWindow)
        self.confirm_throwing.setObjectName(u"confirm_throwing")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.stack.setStyleSheet(u"background-color: rgb(0, 72, 2);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.301136 rgba(0, 111, 22, 255), stop:0.869318 rgba(0, 182, 120, 255));\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image = QLabel(self.page)
        self.image.setObjectName(u"image")
        self.image.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QSize(400, 400))
        self.image.setLayoutDirection(Qt.LeftToRight)
        self.image.setAutoFillBackground(False)
        self.image.setStyleSheet(u"")
        self.image.setFrameShape(QFrame.Box)
        self.image.setFrameShadow(QFrame.Plain)
        self.image.setLineWidth(13)
        self.image.setMidLineWidth(0)
        self.image.setPixmap(QPixmap(u"../../../../../../../../../Desktop/studia/projekt zespo\u0142owy/logo/logo.png"))
        self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.image, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.add_user = QPushButton(self.page)
        self.add_user.setObjectName(u"add_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_user.sizePolicy().hasHeightForWidth())
        self.add_user.setSizePolicy(sizePolicy1)
        self.add_user.setMinimumSize(QSize(0, 40))
        self.add_user.setLayoutDirection(Qt.LeftToRight)
        self.add_user.setStyleSheet(u"background-color: rgb(173, 72, 0);\n"
"\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"\n"
"")

        self.verticalLayout.addWidget(self.add_user, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.add_bin = QPushButton(self.page)
        self.add_bin.setObjectName(u"add_bin")
        sizePolicy1.setHeightForWidth(self.add_bin.sizePolicy().hasHeightForWidth())
        self.add_bin.setSizePolicy(sizePolicy1)
        self.add_bin.setMinimumSize(QSize(0, 40))
        self.add_bin.setLayoutDirection(Qt.LeftToRight)
        self.add_bin.setStyleSheet(u"background-color: rgb(173, 72, 0);\n"
"\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"\n"
"")

        self.verticalLayout.addWidget(self.add_bin, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.news = QLabel(self.page)
        self.news.setObjectName(u"news")
        self.news.setMinimumSize(QSize(200, 76))
        self.news.setStyleSheet(u"\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.news.setFrameShape(QFrame.Box)
        self.news.setLineWidth(2)
        self.news.setMidLineWidth(0)
        self.news.setTextFormat(Qt.PlainText)
        self.news.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.news)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(18, 32, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.page_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.users_list = QListWidget(self.splitter)
        self.users_list.setObjectName(u"users_list")
        self.users_list.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(252, 105, 0);\n"
"\n"
"")
        self.users_list.setLineWidth(1)
        self.users_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.users_list.setTextElideMode(Qt.ElideLeft)
        self.users_list.setResizeMode(QListView.Fixed)
        self.users_list.setSpacing(0)
        self.splitter.addWidget(self.users_list)
        self.user_info = QLabel(self.splitter)
        self.user_info.setObjectName(u"user_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.user_info.sizePolicy().hasHeightForWidth())
        self.user_info.setSizePolicy(sizePolicy2)
        self.user_info.setStyleSheet(u"font: 24pt \"Arial\";\n"
"background-color: rgb(255, 170, 0);")
        self.user_info.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.user_info)

        self.horizontalLayout.addWidget(self.splitter)

        self.stack.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1128, 824))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ranking_list = QLabel(self.scrollAreaWidgetContents)
        self.ranking_list.setObjectName(u"ranking_list")
        self.ranking_list.setStyleSheet(u"font: 36pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.301136 rgba(255, 205, 0, 255), stop:0.869318 rgba(236, 111, 19, 255));\n"
"")
        self.ranking_list.setTextFormat(Qt.PlainText)
        self.ranking_list.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.ranking_list, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 204, 0);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.full_trash_list = QListWidget(self.page_4)
        self.full_trash_list.setObjectName(u"full_trash_list")
        self.full_trash_list.setStyleSheet(u"background-color: rgb(245, 143, 0);\n"
"font: 20pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.full_trash_list)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_10 = QSpacerItem(20, 154, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.stack_volunteer = QStackedWidget(self.page_4)
        self.stack_volunteer.setObjectName(u"stack_volunteer")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stack_volunteer.sizePolicy().hasHeightForWidth())
        self.stack_volunteer.setSizePolicy(sizePolicy3)
        self.stack_volunteer.setMinimumSize(QSize(0, 400))
        self.stack_volunteer.setStyleSheet(u"background-color: rgb(0, 149, 82);\n"
"background-color: rgb(0, 140, 56);\n"
"")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stack_volunteer.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_3 = QHBoxLayout(self.page_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.throw_info = QLabel(self.page_6)
        self.throw_info.setObjectName(u"throw_info")
        self.throw_info.setStyleSheet(u"background-color: rgb(255, 204, 0);\n"
"font: 20pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.throw_info)

        self.users_list_throw = QListWidget(self.page_6)
        self.users_list_throw.setObjectName(u"users_list_throw")
        self.users_list_throw.setStyleSheet(u"background-color: rgb(245, 143, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";")

        self.verticalLayout_8.addWidget(self.users_list_throw)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.volunteer_to_throw = QPushButton(self.page_6)
        self.volunteer_to_throw.setObjectName(u"volunteer_to_throw")
        self.volunteer_to_throw.setMinimumSize(QSize(140, 50))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.volunteer_to_throw.setFont(font)
        self.volunteer_to_throw.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 75 24pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.volunteer_to_throw, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.stack_volunteer.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_5 = QGridLayout(self.page_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.volunteer_info = QLabel(self.page_7)
        self.volunteer_info.setObjectName(u"volunteer_info")
        sizePolicy.setHeightForWidth(self.volunteer_info.sizePolicy().hasHeightForWidth())
        self.volunteer_info.setSizePolicy(sizePolicy)
        self.volunteer_info.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.volunteer_info.setFont(font1)
        self.volunteer_info.setStyleSheet(u"background-color: rgb(255, 204, 0);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.volunteer_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.volunteer_info)

        self.verticalSpacer_7 = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.password = QLineEdit(self.page_7)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(16777215, 50))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet(u"background-color: rgb(255, 188, 105);\n"
"background-color: rgb(255, 163, 35);")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.confirm = QPushButton(self.page_7)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setMinimumSize(QSize(0, 40))
        self.confirm.setStyleSheet(u"\n"
"background-color: rgb(255, 122, 5);")

        self.horizontalLayout_4.addWidget(self.confirm)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.cancel = QPushButton(self.page_7)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(0, 40))
        self.cancel.setStyleSheet(u"background-color: rgb(255, 122, 5);\n"
"")

        self.horizontalLayout_4.addWidget(self.cancel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.error_confirmation = QLabel(self.page_7)
        self.error_confirmation.setObjectName(u"error_confirmation")
        sizePolicy.setHeightForWidth(self.error_confirmation.sizePolicy().hasHeightForWidth())
        self.error_confirmation.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.error_confirmation)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.stack_volunteer.addWidget(self.page_7)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_8 = QGridLayout(self.page_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.info_confirmation_2 = QLabel(self.page_11)
        self.info_confirmation_2.setObjectName(u"info_confirmation_2")
        sizePolicy.setHeightForWidth(self.info_confirmation_2.sizePolicy().hasHeightForWidth())
        self.info_confirmation_2.setSizePolicy(sizePolicy)
        self.info_confirmation_2.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")
        self.info_confirmation_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.info_confirmation_2, 0, 0, 1, 1)

        self.stack_volunteer.addWidget(self.page_11)

        self.verticalLayout_7.addWidget(self.stack_volunteer)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.stack.addWidget(self.page_4)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.horizontalLayout_6 = QHBoxLayout(self.page_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bins_volunteered_list = QListWidget(self.page_8)
        self.bins_volunteered_list.setObjectName(u"bins_volunteered_list")
        self.bins_volunteered_list.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 149, 1);")

        self.horizontalLayout_6.addWidget(self.bins_volunteered_list)

        self.stack_confirm_throwing = QStackedWidget(self.page_8)
        self.stack_confirm_throwing.setObjectName(u"stack_confirm_throwing")
        self.stack_confirm_throwing.setStyleSheet(u"background-color: rgb(255, 213, 2);\n"
"background-color: rgb(249, 179, 1);")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_6 = QGridLayout(self.page_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_3 = QLabel(self.page_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.stack_confirm_throwing.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_7 = QGridLayout(self.page_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bin_info = QLabel(self.page_10)
        self.bin_info.setObjectName(u"bin_info")

        self.gridLayout_7.addWidget(self.bin_info, 0, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_7.addItem(self.verticalSpacer_11, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.confirm_throwed = QPushButton(self.page_10)
        self.confirm_throwed.setObjectName(u"confirm_throwed")
        self.confirm_throwed.setMinimumSize(QSize(0, 50))
        self.confirm_throwed.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_7.addWidget(self.confirm_throwed)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.gridLayout_7.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.message = QLabel(self.page_10)
        self.message.setObjectName(u"message")
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.message, 2, 0, 1, 1)

        self.stack_confirm_throwing.addWidget(self.page_10)

        self.horizontalLayout_6.addWidget(self.stack_confirm_throwing)

        self.stack.addWidget(self.page_8)

        self.gridLayout_2.addWidget(self.stack, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1166, 21))
        self.menuuser = QMenu(self.menubar)
        self.menuuser.setObjectName(u"menuuser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuuser.menuAction())
        self.menuuser.addAction(self.main)
        self.menuuser.addAction(self.users)
        self.menuuser.addAction(self.ranking)
        self.menuuser.addAction(self.throw_trash)
        self.menuuser.addAction(self.confirm_throwing)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(0)
        self.stack_volunteer.setCurrentIndex(2)
        self.stack_confirm_throwing.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MINKA", None))
        self.users.setText(QCoreApplication.translate("MainWindow", u"u\u017cytkownicy", None))
        self.ranking.setText(QCoreApplication.translate("MainWindow", u"ranking", None))
        self.trash_bin.setText(QCoreApplication.translate("MainWindow", u"trash bin", None))
        self.throw_trash.setText(QCoreApplication.translate("MainWindow", u"wyrzu\u0107 \u015bmieci", None))
        self.main.setText(QCoreApplication.translate("MainWindow", u"strona g\u0142\u00f3wna", None))
        self.confirm_throwing.setText(QCoreApplication.translate("MainWindow", u"potwierd\u017a wyrzucenie", None))
        self.image.setText("")
        self.add_user.setText(QCoreApplication.translate("MainWindow", u"dodaj u\u017cytkownika", None))
        self.add_bin.setText(QCoreApplication.translate("MainWindow", u"dodaj kosz", None))
        self.news.setText(QCoreApplication.translate("MainWindow", u"Informacje", None))
        self.user_info.setText("")
        self.ranking_list.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz \u015bmietnik do kt\u00f3rego\n"
"wyrzucania chcesz si\u0119 zg\u0142osi\u0107", None))
        self.throw_info.setText(QCoreApplication.translate("MainWindow", u"Wybierz siebie z listy", None))
        self.volunteer_to_throw.setText(QCoreApplication.translate("MainWindow", u"Zg\u0142o\u015b si\u0119", None))
        self.volunteer_info.setText(QCoreApplication.translate("MainWindow", u"Wpisz swoje has\u0142o", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Potwierd\u017a", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.error_confirmation.setText("")
        self.info_confirmation_2.setText(QCoreApplication.translate("MainWindow", u"Zg\u0142oszenie zosta\u0142o zapisane", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wybierz \u015bmietnik, kt\u00f3rego wyrzucenie\n"
"\u015bmieci chcesz potwierdzi\u0107", None))
        self.bin_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.confirm_throwed.setText(QCoreApplication.translate("MainWindow", u"Potwierd\u017a", None))
        self.message.setText(QCoreApplication.translate("MainWindow", u"message", None))
        self.menuuser.setTitle(QCoreApplication.translate("MainWindow", u"menu", None))
    # retranslateUi

