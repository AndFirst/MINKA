# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_bin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BinDialog(object):
    def setupUi(self, BinDialog):
        if not BinDialog.objectName():
            BinDialog.setObjectName(u"BinDialog")
        BinDialog.resize(488, 371)
        BinDialog.setStyleSheet(u"background-color: rgb(18, 199, 108);")
        self.gridLayout = QGridLayout(BinDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label = QLabel(BinDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 22pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(BinDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(255, 119, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 0, 1, 2, Qt.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(BinDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_4)

        self.apartment = QLineEdit(BinDialog)
        self.apartment.setObjectName(u"apartment")
        self.apartment.setMinimumSize(QSize(0, 30))
        self.apartment.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 184, 2);")

        self.verticalLayout_2.addWidget(self.apartment)

        self.empty_apartment_error = QLabel(BinDialog)
        self.empty_apartment_error.setObjectName(u"empty_apartment_error")
        self.empty_apartment_error.setTextFormat(Qt.RichText)

        self.verticalLayout_2.addWidget(self.empty_apartment_error)


        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(BinDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_3)

        self.id = QLineEdit(BinDialog)
        self.id.setObjectName(u"id")
        self.id.setMinimumSize(QSize(0, 30))
        self.id.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 184, 2);")

        self.verticalLayout.addWidget(self.id)

        self.empty_id_error = QLabel(BinDialog)
        self.empty_id_error.setObjectName(u"empty_id_error")

        self.verticalLayout.addWidget(self.empty_id_error)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)


        self.retranslateUi(BinDialog)
        self.buttonBox.accepted.connect(BinDialog.accept)
        self.buttonBox.rejected.connect(BinDialog.reject)

        QMetaObject.connectSlotsByName(BinDialog)
    # setupUi

    def retranslateUi(self, BinDialog):
        BinDialog.setWindowTitle(QCoreApplication.translate("BinDialog", u"Dodaj kosz", None))
        self.label.setText(QCoreApplication.translate("BinDialog", u"Dodaj Kosz", None))
        self.label_4.setText(QCoreApplication.translate("BinDialog", u"Mieszkanie", None))
        self.empty_apartment_error.setText("")
        self.label_3.setText(QCoreApplication.translate("BinDialog", u"Id", None))
        self.empty_id_error.setText("")
    # retranslateUi

