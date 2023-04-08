# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full_trash.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Message(object):
    def setupUi(self, Message):
        if not Message.objectName():
            Message.setObjectName(u"Message")
        Message.resize(434, 154)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Message.sizePolicy().hasHeightForWidth())
        Message.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Message)
        self.gridLayout.setObjectName(u"gridLayout")
        self.message = QLabel(Message)
        self.message.setObjectName(u"message")
        self.message.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.message.setTextFormat(Qt.PlainText)

        self.gridLayout.addWidget(self.message, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Message)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Message)
        self.buttonBox.accepted.connect(Message.accept)
        self.buttonBox.rejected.connect(Message.reject)

        QMetaObject.connectSlotsByName(Message)
    # setupUi

    def retranslateUi(self, Message):
        Message.setWindowTitle(QCoreApplication.translate("Message", u"Dialog", None))
        self.message.setText("")
    # retranslateUi

