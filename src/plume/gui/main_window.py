# -*- coding: utf-8 -*-
'''
Created on 25 avr. 2015

@author: Cyril Jacquet
'''

from PyQt5.QtWidgets import (QMainWindow, QWidget, QActionGroup, QToolBar, QWidgetAction,
                             QHBoxLayout,  QFileDialog, QMessageBox,  QApplication, QUndoView)
from PyQt5.QtCore import Qt,  QDir, QDate
from .window_system import WindowSystemController
from .write_panel import WritePanel
from .note_panel import NotePanel
from .binder_panel import BinderPanel
from .table_panel import TablePanel
from .cards_panel import CardsPanel
from .info_panel import InfoPanel
from .welcome_panel import WelcomePanel
from PyQt5.Qt import QToolButton, pyqtSlot, QUndoGroup, QSettings, QByteArray
from . import cfg
from .main_window_ui import Ui_MainWindow
from .preferences import Preferences
from .about_plume import AboutPlume
from .signal_hub import SignalHub
import os.path


class MainWindow(QMainWindow, WindowSystemController):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui()
        cfg.window = self

        cfg.data_subscriber.subscribe_update_func_to_domain(0, self._clear_project,  "database_closed")
        cfg.data_subscriber.subscribe_update_func_to_domain(0, self._activate,  "database_loaded")
        cfg.data.subscriber.subscribe_update_func_to_domain(0, self.set_project_is_saved, "database_saved")
        # cfg.core.subscriber.subscribe_update_func_to_domain(
        #     self.set_project_is_not_saved, "core.project.notsaved")

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        widget = QWidget()
        layout = QHBoxLayout()

        self.stackWidget = SubWindowStack(self)
        self.side_bar = SideBar(self)
        # self.side_bar.detach_signal.connect(self.detach_window)

        layout.addWidget(self.side_bar)
        layout.addWidget(self.stackWidget)
        # layout.addWidget(self.sub_window)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        cfg.undo_group = QUndoGroup(self)
        cfg.signal_hub = SignalHub(self)

        # window system :
        self.window_system_parent_widget = self.stackWidget
        self.side_bar.window_system_controller = self

        # sub_windows :
        self._sub_window_action_group = QActionGroup(self)

        # welcome window
        self.welcome_panel = WelcomePanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.welcome_panel)
        self.ui.actionWelcome.setProperty(
            "sub_window_object_name", "welcome_panel")
        self.add_action_to_window_system(self.ui.actionWelcome)
        self._sub_window_action_group.addAction(self.ui.actionWelcome)


        # write window
        self.write_panel = WritePanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.write_panel)
        self.ui.actionWrite.setProperty(
            "sub_window_object_name", "write_panel")
        self.add_action_to_window_system(self.ui.actionWrite)
        self._sub_window_action_group.addAction(self.ui.actionWrite)

        # note panel window
        self.note_panel = NotePanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.note_panel)
        self.ui.actionNote.setProperty(
            "sub_window_object_name", "note_panel")
        self.add_action_to_window_system(self.ui.actionNote)
        self._sub_window_action_group.addAction(self.ui.actionNote)

        # TODO: set the below panels as internal plugins

        # binder panel window
        self.binder_panel = BinderPanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.binder_panel)
        self.ui.actionBinder.setProperty(
            "sub_window_object_name", "binder_panel")
        self.add_action_to_window_system(self.ui.actionBinder)
        self._sub_window_action_group.addAction(self.ui.actionBinder)

         # table panel window
        self.table_panel = TablePanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.table_panel)
        self.ui.actionTable.setProperty(
            "sub_window_object_name", "table_panel")
        self.add_action_to_window_system(self.ui.actionTable)
        self._sub_window_action_group.addAction(self.ui.actionTable)

        # cards panel window
        self.cards_panel = CardsPanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.cards_panel)
        self.ui.actionCards.setProperty(
            "sub_window_object_name", "cards_panel")
        self.add_action_to_window_system(self.ui.actionCards)
        self._sub_window_action_group.addAction(self.ui.actionCards)

        # info panel window
        self.info_panel = InfoPanel(
            parent=self, parent_window_system_controller=self)
        self.attach_sub_window(self.info_panel)
        self.ui.actionInfo.setProperty(
            "sub_window_object_name", "info_panel")
        self.add_action_to_window_system(self.ui.actionInfo)
        self._sub_window_action_group.addAction(self.ui.actionInfo)

       # switch to Write panel by default
        self.ui.actionWelcome.trigger()




        # menu bar actions
        self.ui.actionOpen_test_project.triggered.connect(
            self.launch_open_test_project)
        self.ui.actionPreferences.triggered.connect(self.launch_preferences)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave_as.triggered.connect(self.launch_save_as_dialog)
        self.ui.actionOpen.triggered.connect(self.launch_open_dialog)
        self.ui.actionClose_project.triggered.connect(self.launch_close_dialog)
        self.ui.actionExit.triggered.connect(self.launch_exit_dialog)

        # Help menu actions
        self.ui.actionAbout_Plume_Creator.triggered.connect(self.about_Plume)
        self.ui.actionAbout_Qt.triggered.connect(QApplication.instance().aboutQt)

        self._activate(False)

        self.apply_settings()

    @pyqtSlot()
    def apply_settings(self):
        settings = QSettings()
        self.restoreGeometry((settings.value("main_window/geometry", QByteArray())))

    def set_application_arguments(self, arguments):
        project_opened_in_arg = False
        for arg in arguments:
            if arg[0] is "-":  # actions if other arguments
                pass
            elif os.path.exists(arg):
                cfg.data.load_database(0, arg)
                project_opened_in_arg = True

        # TODO open default project
        # if not project_opened_in_arg:
        #     cfg.data.load_database(0, "")  # opens empty default project


    @pyqtSlot()
    def launch_open_test_project(self):
        if cfg.data.is_database_open(0):
            if self.launch_close_dialog() == QMessageBox.Cancel:
                return
        cfg.data.load_database(0, '../../resources/plume_test_project.sqlite')

        # set default save path other than test project file itself
        from os.path import expanduser
        home = expanduser("~")
        database = cfg.data.get_database(0)
        database.path = os.path.join(home, "test_project.sqlite")

        self.setWindowTitle("Plume Creator - TEST")

        # switch to Write panel
        self.ui.actionWrite.trigger()

        # self.undo_view = QUndoView(cfg.undo_group, None)
        # self.undo_view.show()

    @pyqtSlot()
    def launch_preferences(self):
        pref = Preferences(self)
        pref.exec_()

    @pyqtSlot()
    def launch_save_as_dialog(self):
        working_directory = QDir.homePath()
        fileName, selectedFilter = QFileDialog.getSaveFileName(
            self,
            _("Save as"),
            working_directory,
            _("Databases (*.sqlite *.plume);;All files (*)"),
            _(".sqlite"))
        if fileName is None:
            return
        cfg.data.save_database(0, fileName) # ,  selectedFilter

    @pyqtSlot()
    def save(self):
        cfg.data.save_database(0, cfg.data.database.path)

    @pyqtSlot()
    def launch_open_dialog(self):
        working_directory = QDir().homePath()
        fileName, selectedFilter = QFileDialog.getOpenFileName(
            self,
            _("Open"),
            working_directory,
            _("Databases (*.sqlite *.plume);;All files (*)"),
            _(".sqlite"))

        if fileName is None:
            return
        if cfg.data.is_database_open:
            if self.launch_close_dialog() == QMessageBox.Cancel:
                return
        cfg.data.load_database(0, fileName)

        self.setWindowTitle("Plume Creator - " + fileName)

        # switch to Write panel
        self.ui.actionWrite.trigger()

    @pyqtSlot()
    def launch_close_dialog(self):
        if not cfg.data.is_database_open:
            return

        result = QMessageBox.question(
            self,
            _("Close the current project"),
            _("The last changes are not yet saved. Do you really want to close the current project ?"),
            QMessageBox.StandardButtons(
                QMessageBox.Cancel |
                QMessageBox.Discard |
                QMessageBox.Save),
            QMessageBox.Cancel)

        if result == QMessageBox.Cancel:
            return QMessageBox.Cancel
        elif result == QMessageBox.Discard:
            cfg.data.close_database(0)
        elif result == QMessageBox.Save:
            cfg.data.save_database(0, cfg.data.database.path)
            cfg.data.close_database(0)

    @pyqtSlot()
    def launch_exit_dialog(self):
        if cfg.data.is_database_open(0) == False:
            QApplication.quit()

        result = self.launch_close_dialog()
        if result == QMessageBox.Cancel:
            return QMessageBox.Cancel
        QApplication.quit()

    @pyqtSlot()
    def about_Plume(self):
        about = AboutPlume(self)
        about.exec_()


    def set_project_is_saved(self):
        self.ui.actionSave.setEnabled(False)

    def set_project_is_not_saved(self):
        self.ui.actionSave.setEnabled(True)

    def _clear_project(self):
        self.setWindowTitle("Plume Creator")
        self._activate(False)

    def _activate(self, value=True):
        self.ui.actionSave_as.setEnabled(value)
        self.ui.actionSave.setEnabled(value)
        self.ui.actionClose_project.setEnabled(value)
        self.ui.actionImport.setEnabled(value)
        self.ui.actionExport.setEnabled(value)
        self.ui.actionPrint.setEnabled(value)

    def closeEvent(self,  event):
        result = self.launch_exit_dialog()
        if result == QMessageBox.Cancel:
            event.ignore()
        else:
            QSettings().setValue("main_window/geometry", self.saveGeometry())
            event.accept()


from PyQt5.QtWidgets import QStackedWidget
from .window_system import WindowSystemParentWidget


class SubWindowStack(QStackedWidget, WindowSystemParentWidget):

    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(SubWindowStack, self).__init__(parent)

    def attach_sub_window(self, sub_window):
        WindowSystemParentWidget.attach_sub_window(self, sub_window)
        self.addWidget(sub_window)

    def detach_sub_window(self, sub_window):
        WindowSystemParentWidget.detach_sub_window(self, sub_window)

    def set_sub_window_visible(self, sub_window):
        WindowSystemParentWidget.set_sub_window_visible(self, sub_window)
        if sub_window.isWindow():
            sub_window.setWindowState(
                sub_window.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            sub_window.activateWindow()
        else:
            self.setCurrentWidget(sub_window)


from .window_system import WindowSystemActionHandler
from PyQt5.QtWidgets import QToolButton, QMenu,  QSizePolicy
from PyQt5.QtCore import QSize
from .side_bar_ui import Ui_SideBar


class SideBar(QWidget, WindowSystemActionHandler):

    # detach_signal = QtCore.pyqtSignal(QMainWindow)

    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)
        self.ui = Ui_SideBar()
        self.ui.setupUi(self)

        self.side_bar_button_list = []

    @pyqtSlot()
    def onDetachClicked(self):
        '''
        Must only be used as a slot for Qt signals !
        '''
        self.detach_sub_window()
        for button in self.side_bar_button_list:
            if button.property("sub_window_object_name") != self.sender().property("sub_window_object_name"):
                button.click()
                break

    @pyqtSlot()
    def onAttachClicked(self):
        '''
        Must only be used as a slot for Qt signals !
        '''
        self.attach_sub_window()
        for button in self.side_bar_button_list:
            if button.property("sub_window_object_name") == self.sender().property("sub_window_object_name"):
                button.click()

    @pyqtSlot(bool)
    def action_toggled_slot(self, value):
        '''
        Must only be used as a slot for Qt signals !
        '''
        if value is True:
            self.set_sub_window_visible()
#            for button in self.side_bar_button_list:
#                if button.property("sub_window_object_name") != self.sender().property("sub_window_object_name"):
#                    button.setChecked(True)
#                    break

    @pyqtSlot()
    def set_sub_window_visible(self):
        '''
        Must only be used as a slot for Qt signals !
        '''
        sub_window = self.get_sub_window_linked_to_action(self.sender())
        self.window_system_controller.window_system_parent_widget.set_sub_window_visible(
            sub_window)

    def clear(self):
        for button in self.side_bar_button_list:
            self.side_bar_button_list.remove(button)
            button.deleteLater()
        self.side_bar_button_list = []

    def update_from_window_system_ctrl(self):

        class SideBarButton(QToolButton):

            def __init__(self, parent, action):
                super(SideBarButton, self).__init__(parent)
                self.setCheckable(True)
                self.setAutoRaise(True)
                self.setIconSize(QSize(40, 40))
                self.setFixedSize(60, 60)
                self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                self.setDefaultAction(action)
                self._prop = action.property("sub_window_object_name")
                self.setProperty("sub_window_object_name", self._prop)

            def contextMenuEvent(self, event):
                menu = QMenu(self)
                attachAction = menu.addAction("Attach")
                attachAction.setProperty("sub_window_object_name", self._prop)
                attachAction.triggered.connect(self.parent().onAttachClicked)
                detachAction = menu.addAction("Detach")
                detachAction.setProperty("sub_window_object_name", self._prop)
                detachAction.triggered.connect(self.parent().onDetachClicked)
                menu.exec_(self.mapToGlobal(event.pos()))

                return QToolButton.contextMenuEvent(self, event)


        WindowSystemActionHandler.update_from_window_system_ctrl(self)
        self.clear()

        for action in self._sub_window_action_list:
            action.setCheckable(True)
            action.toggled.connect(self.action_toggled_slot)

            button = SideBarButton(self, action)
            self.side_bar_button_list.append(button)
            self.ui.actionLayout.addWidget(button)
            self.side_bar_button_list.append(button)
