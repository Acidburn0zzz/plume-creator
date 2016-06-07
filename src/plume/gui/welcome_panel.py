from .sub_window import SubWindow
from .welcome_panel_ui import Ui_WelcomePanel


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


