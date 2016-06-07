from .sub_window import SubWindow
from .info_panel_ui import Ui_InfoPanel


class InfoPanel(SubWindow):

    '''
    'Info' main panel. Detachable
    '''

    def __init__(self, parent, parent_window_system_controller):
        '''

        '''
        super(InfoPanel, self).__init__(
            parent=parent, parent_window_system_controller=parent_window_system_controller)

        self.ui = Ui_InfoPanel()
        self.ui.setupUi(self)
        self.setWindowTitle(_("Info"))
        self.setObjectName("info_panel")
