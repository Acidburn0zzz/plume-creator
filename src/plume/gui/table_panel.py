from .sub_window import SubWindow
from .table_panel_ui import Ui_TablePanel
from . import cfg


class TablePanel(SubWindow):

    '''
    'Table' main panel. Detachable
    '''

    def __init__(self, parent, parent_window_system_controller):
        '''

        '''
        super(TablePanel, self).__init__(
            parent=parent, parent_window_system_controller=parent_window_system_controller)

        self.ui = Ui_TablePanel()
        self.ui.setupUi(self)
        self.setWindowTitle(_("Table"))
        self.setObjectName("table_panel")

        self._write_tree_model = cfg.models["0_sheet_tree_model"]
        self.ui.treeView.setModel(self._write_tree_model)

