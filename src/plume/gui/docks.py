'''
Created on 7 mai 2015

@author:  Cyril Jacquet
'''
from PyQt5.QtWidgets import QDockWidget, QWidget
from PyQt5.Qt import pyqtSlot, QObject
from . import cfg
from PyQt5.QtCore import Qt
from enum import Enum


class DockSystem(QObject):

    '''

    DockSystem
    For now, it's only for the write_tree docks
    '''
    DockTypes = Enum('DockType', 'WriteSubWindowDock WritePanelDock NotePanelDock NoteSubWindowDock')

    def __init__(self, parent, main_window,  dock_type):
        '''
        Constructor
        '''

        super(DockSystem, self).__init__(parent)
        self._paper_id = None
        self.main_window = main_window
        self.dock_list = []

        if dock_type is self.DockTypes.WriteSubWindowDock:
            self._default_dock = "write-properties-dock"
            write_subwindow_dock_plugin_dict = cfg.gui_plugins.write_subwindow_dock_plugin_dict
            # add there other dicts with built-in docks
            self.dock_type_dict = write_subwindow_dock_plugin_dict

        if dock_type is self.DockTypes.WritePanelDock:
            self._default_dock = "write-tree-dock"
            write_panel_dock_plugin_dict = cfg.gui_plugins.write_panel_dock_plugin_dict
            # add there other dicts with built-in docks
            self.dock_type_dict = write_panel_dock_plugin_dict

        if dock_type is self.DockTypes.NoteSubWindowDock:
            self._default_dock = "note-properties-dock"
            note_subwindow_dock_plugin_dict = cfg.gui_plugins.note_subwindow_dock_plugin_dict
            # add there other dicts with built-in docks
            self.dock_type_dict = note_subwindow_dock_plugin_dict

        if dock_type is self.DockTypes.NotePanelDock:
            self._default_dock = "note-tree-dock"
            note_panel_dock_plugin_dict = cfg.gui_plugins.note_panel_dock_plugin_dict
            # add there other dicts with built-in docks
            self.dock_type_dict = note_panel_dock_plugin_dict


    def split_dock(self, dock):
        '''
        function:: split_dock(dock)
        :param dock:
        '''
        area = self.main_window.dockWidgetArea(dock)
        self.add_dock(dock.current_type, area)


    def add_dock(self, type_str, area=Qt.RightDockWidgetArea):
        '''
        function:: add_dock(type, zone)
        :param type_str: type of dock
        :param zone:
        '''

        dock = DockTemplate(self, dock_system=self)
        self.change_type(dock, type_str)
        self.dock_list.append(dock)

        self.main_window.addDockWidget(area, dock)

    def change_type(self, dock, type_str):
        '''
        function:: change_type(dock, type_str)
        :param dock:
        :param type_str:
        '''
        gui_part = self.dock_type_dict[type_str]
        gui_part = gui_part()
        gui_part.paper_id = self.paper_id
        widget = gui_part.get_widget()
        dock.current_type = type_str
        dock.setWindowTitle(gui_part.dock_displayed_name)
        dock.setObjectName(gui_part.dock_displayed_name)
        dock.setWidget(widget)
        dock.titleBarWidget().ui.comboBox.setCurrentText(
            gui_part.dock_displayed_name)

    def remove_dock(self, dock):
        '''
        function:: remove_dock(dock)
        :param dock:
        '''
        self.dock_list.remove(dock)
        dock.close()
        dock.deleteLater()

    @property
    def paper_id(self):
        return self._paper_id

    @paper_id.setter
    def paper_id(self, paper_id):
        self._paper_id = paper_id
        if self._paper_id is not None:
            for dock in self.dock_list:  # update all docks' sheet_id
                dock.widget().gui_part.paper_id = paper_id

    def load_settings(self):
        '''
        function:: load_settings()
        :param :
        '''

        pass

    def save_settings(self):
        '''
        function:: save_settings()
        :param :
        '''

        pass


class DockTemplate(QDockWidget):

    '''
    DockTemplate
    '''

    def __init__(self, parent=None, dock_system=None):
        '''
        Constructor
        '''

        super(DockTemplate, self).__init__(parent=None)
        self.current_type = None
        title_widget = DockTitleWidget(self, self)
        self.setTitleBarWidget(title_widget)
        self.dock_system = dock_system

        self.setFeatures(self.features() | (QDockWidget.DockWidgetFloatable |
                                            QDockWidget.DockWidgetMovable))

    @property
    def dock_system(self):
        return self._dock_system

    @dock_system.setter
    def dock_system(self, dock_system):
        if dock_system is not None:
            self._dock_system = dock_system
            self.titleBarWidget().fill_comboBox_with_types()

    def split(self):
        self.dock_system.split_dock(self)

from .dock_title_bar_ui import Ui_DockTitleBar


class DockTitleWidget(QWidget):

    '''
    DockTitleWidget
    '''

    def __init__(self, parent_dock, parent=None):
        '''
        Constructor
        '''

        super(DockTitleWidget, self).__init__(parent=None)
        self.parent_dock = parent_dock
        self.ui = Ui_DockTitleBar()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.parent_dock.close()

    @pyqtSlot()
    def on_addDockButton_clicked(self):
        if self.parent_dock is None:
            return
        self.parent_dock.split()

    def fill_comboBox_with_types(self):
        # types_name_dict = {}
        self.ui.comboBox.disconnect()
        gui_parts = self.parent_dock.dock_system.dock_type_dict.values()
        for part in gui_parts:
            # types_name_dict[part.dock_displayed_name] = part.dock_name
            self.ui.comboBox.addItem(
                part.dock_displayed_name, userData=part.dock_name)
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

    @pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        # print(self.ui.comboBox.itemData(index, Qt.UserRole))

        if self.parent_dock is None:
            return
        dock_type = self.ui.comboBox.itemData(index, Qt.UserRole)
        if self.parent_dock.current_type == dock_type:
            return
        self.parent_dock.dock_system.change_type(self.parent_dock,  dock_type)
