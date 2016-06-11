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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName("formLayout_2")
        self.authorLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.backCoverLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.backCoverLabel.setObjectName("backCoverLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.backCoverLabel)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        InfoPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(InfoPanel)
        QtCore.QMetaObject.connectSlotsByName(InfoPanel)

    def retranslateUi(self, InfoPanel):

        InfoPanel.setWindowTitle(_("MainWindow"))
        self.authorLabel.setText(_("Author"))
        self.backCoverLabel.setText(_("Back cover"))

