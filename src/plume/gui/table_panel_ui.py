# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/table_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TablePanel(object):
    def setupUi(self, TablePanel):
        TablePanel.setObjectName("TablePanel")
        TablePanel.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TablePanel)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        TablePanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(TablePanel)
        QtCore.QMetaObject.connectSlotsByName(TablePanel)

    def retranslateUi(self, TablePanel):

        TablePanel.setWindowTitle(_("MainWindow"))

