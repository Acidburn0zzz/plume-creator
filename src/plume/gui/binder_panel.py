from .sub_window import SubWindow
from .binder_panel_ui import Ui_BinderPanel


class BinderPanel(SubWindow):

    '''
    'Binder' main panel. Detachable
    '''

    def __init__(self, parent, parent_window_system_controller):
        '''

        '''
        super(BinderPanel, self).__init__(
            parent=parent, parent_window_system_controller=parent_window_system_controller)

        self.ui = Ui_BinderPanel()
        self.ui.setupUi(self)
        self.setWindowTitle(_("Binder"))
        self.setObjectName("binder_panel")
