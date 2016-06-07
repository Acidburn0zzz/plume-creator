from .sub_window import SubWindow
from .cards_panel_ui import Ui_CardsPanel


class CardsPanel(SubWindow):

    '''
    'Cards' main panel. Detachable
    '''

    def __init__(self, parent, parent_window_system_controller):
        '''

        '''
        super(CardsPanel, self).__init__(
            parent=parent, parent_window_system_controller=parent_window_system_controller)

        self.ui = Ui_CardsPanel()
        self.ui.setupUi(self)
        self.setWindowTitle(_("Cards"))
        self.setObjectName("cards_panel")
