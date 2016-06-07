# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/welcome_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomePanel(object):
    def setupUi(self, WelcomePanel):
        WelcomePanel.setObjectName("WelcomePanel")
        WelcomePanel.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WelcomePanel)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.verticalLayout.addWidget(self.quickWidget)
        WelcomePanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomePanel)
        QtCore.QMetaObject.connectSlotsByName(WelcomePanel)

    def retranslateUi(self, WelcomePanel):

        WelcomePanel.setWindowTitle(_("MainWindow"))

from PyQt5 import QtQuickWidgets
