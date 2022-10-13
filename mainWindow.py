# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowneVMbf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 60, 171, 19))
        self.cbET = QCheckBox(self.centralwidget)
        self.cbET.setObjectName(u"cbET")
        self.cbET.setGeometry(QRect(120, 320, 131, 23))
        self.cbPC = QCheckBox(self.centralwidget)
        self.cbPC.setObjectName(u"cbPC")
        self.cbPC.setGeometry(QRect(240, 320, 131, 23))
        self.cbWS = QCheckBox(self.centralwidget)
        self.cbWS.setObjectName(u"cbWS")
        self.cbWS.setGeometry(QRect(370, 320, 131, 23))
        self.cbSC = QCheckBox(self.centralwidget)
        self.cbSC.setObjectName(u"cbSC")
        self.cbSC.setGeometry(QRect(490, 320, 141, 23))
        self.pbSelect = QPushButton(self.centralwidget)
        self.pbSelect.setObjectName(u"pbSelect")
        self.pbSelect.setGeometry(QRect(310, 60, 121, 27))
        self.pbRun = QPushButton(self.centralwidget)
        self.pbRun.setObjectName(u"pbRun")
        self.pbRun.setGeometry(QRect(300, 360, 121, 27))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(110, 100, 521, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please select XML files.", None))
        self.cbET.setText(QCoreApplication.translate("MainWindow", u"Empty Tags", None))
        self.cbPC.setText(QCoreApplication.translate("MainWindow", u"P Class  Tags", None))
        self.cbWS.setText(QCoreApplication.translate("MainWindow", u"Whitespaces", None))
        self.cbSC.setText(QCoreApplication.translate("MainWindow", u"Section Content", None))
        self.pbSelect.setText(QCoreApplication.translate("MainWindow", u"Select File(s)", None))
        self.pbRun.setText(QCoreApplication.translate("MainWindow", u"Run Cleanup", None))
    # retranslateUi

