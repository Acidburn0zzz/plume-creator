from .sub_window import SubWindow
from .welcome_panel_ui import Ui_WelcomePanel
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtCore import QUrl
import os, inspect


class WelcomePanel(SubWindow):

    '''
    'Table' main panel. Detachable
    '''

    def __init__(self, parent, parent_window_system_controller):
        '''

        '''
        super(WelcomePanel, self).__init__(
            parent=parent, parent_window_system_controller=parent_window_system_controller)

        self.ui = Ui_WelcomePanel()
        self.ui.setupUi(self)
        self.setWindowTitle(_("Welcome"))
        self.setObjectName("welcome_panel")

        self.ui.quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        #self.ui.quickWidget.rootContext().setContextProperty("myModel", self.filter)
        abspath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.ui.quickWidget.setSource(QUrl(abspath + "/qml/WelcomePanel.qml"))