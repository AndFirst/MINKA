# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_user.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(549, 438)
        Dialog.setStyleSheet(u"background-color: rgb(0, 199, 146);\n"
"background-color: rgb(18, 199, 108);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 119, 0);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 22pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.name = QLineEdit(Dialog)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 30))
        self.name.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 184, 2);")

        self.verticalLayout.addWidget(self.name)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.surname = QLineEdit(Dialog)
        self.surname.setObjectName(u"surname")
        self.surname.setMinimumSize(QSize(0, 30))
        self.surname.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 184, 2);")

        self.verticalLayout_2.addWidget(self.surname)


        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.label_4)

        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 184, 2);")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.password)

        self.empty_password_error = QLabel(Dialog)
        self.empty_password_error.setObjectName(u"empty_password_error")

        self.verticalLayout_3.addWidget(self.empty_password_error)


        self.gridLayout.addLayout(self.verticalLayout_3, 9, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.empty_name_error = QLabel(Dialog)
        self.empty_name_error.setObjectName(u"empty_name_error")
        self.empty_name_error.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.empty_name_error, 3, 0, 1, 1)

        self.empty_surname_error = QLabel(Dialog)
        self.empty_surname_error.setObjectName(u"empty_surname_error")

        self.gridLayout.addWidget(self.empty_surname_error, 6, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dodaj u\u017cytkownika", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Dodaj u\u017cytkownika", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Imi\u0119", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nazwisko", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Has\u0142o", None))
        self.empty_password_error.setText("")
        self.empty_name_error.setText("")
        self.empty_surname_error.setText("")
    # retranslateUi

