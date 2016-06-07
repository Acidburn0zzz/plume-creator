# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/info_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoPanel(object):
    def setupUi(self, InfoPanel):
        InfoPanel.setObjectName("InfoPanel")
        InfoPanel.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(InfoPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        InfoPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(InfoPanel)
        QtCore.QMetaObject.connectSlotsByName(InfoPanel)

    def retranslateUi(self, InfoPanel):

        InfoPanel.setWindowTitle(_("MainWindow"))
        self.pushButton.setText(_("PushButton"))

