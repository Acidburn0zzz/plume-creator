# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/cards_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CardsPanel(object):
    def setupUi(self, CardsPanel):
        CardsPanel.setObjectName("CardsPanel")
        CardsPanel.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CardsPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        CardsPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(CardsPanel)
        QtCore.QMetaObject.connectSlotsByName(CardsPanel)

    def retranslateUi(self, CardsPanel):

        CardsPanel.setWindowTitle(_("MainWindow"))
        self.toolButton.setText(_("..."))

