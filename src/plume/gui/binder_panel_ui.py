# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/binder_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BinderPanel(object):
    def setupUi(self, BinderPanel):
        BinderPanel.setObjectName("BinderPanel")
        BinderPanel.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BinderPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        BinderPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(BinderPanel)
        QtCore.QMetaObject.connectSlotsByName(BinderPanel)

    def retranslateUi(self, BinderPanel):

        BinderPanel.setWindowTitle(_("MainWindow"))
        self.toolButton.setText(_("..."))

