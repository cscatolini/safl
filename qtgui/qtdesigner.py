# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created: Fri Feb 24 16:59:45 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 648)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Centralwidget.sizePolicy().hasHeightForWidth())
        self.Centralwidget.setSizePolicy(sizePolicy)
        self.Centralwidget.setObjectName(_fromUtf8("Centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.im1 = MplWidget(self.Centralwidget)
        self.im1.setObjectName(_fromUtf8("im1"))
        self.horizontalLayout.addWidget(self.im1)
        self.im2 = MplWidget(self.Centralwidget)
        self.im2.setObjectName(_fromUtf8("im2"))
        self.horizontalLayout.addWidget(self.im2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.im3 = MplWidget(self.Centralwidget)
        self.im3.setObjectName(_fromUtf8("im3"))
        self.horizontalLayout_2.addWidget(self.im3)
        self.im4 = MplWidget(self.Centralwidget)
        self.im4.setObjectName(_fromUtf8("im4"))
        self.horizontalLayout_2.addWidget(self.im4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.comboBox = QtGui.QComboBox(self.Centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_3.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.Centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSharingan = QtGui.QMenu(self.menubar)
        self.menuSharingan.setTitle(QtGui.QApplication.translate("MainWindow", "SAFL", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSharingan.setObjectName(_fromUtf8("menuSharingan"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionSelect_File = QtGui.QAction(MainWindow)
        self.actionSelect_File.setText(QtGui.QApplication.translate("MainWindow", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_File.setObjectName(_fromUtf8("actionSelect_File"))
        self.mplactionOpen = QtGui.QAction(MainWindow)
        self.mplactionOpen.setText(QtGui.QApplication.translate("MainWindow", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.mplactionOpen.setObjectName(_fromUtf8("mplactionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.mplactionClose = QtGui.QAction(MainWindow)
        self.mplactionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.mplactionClose.setObjectName(_fromUtf8("mplactionClose"))
        self.actionLoad_Config = QtGui.QAction(MainWindow)
        self.actionLoad_Config.setText(QtGui.QApplication.translate("MainWindow", "Load Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Config.setObjectName(_fromUtf8("actionLoad_Config"))
        self.actionClose_2 = QtGui.QAction(MainWindow)
        self.actionClose_2.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_2.setObjectName(_fromUtf8("actionClose_2"))
        self.menuSharingan.addAction(self.actionLoad_Config)
        self.menuSharingan.addSeparator()
        self.menuSharingan.addAction(self.actionClose_2)
        self.menubar.addAction(self.menuSharingan.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from mplwidget import MplWidget
