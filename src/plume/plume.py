import ui_converter
import qrc_converter
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from data.data import Data
from data import subscriber
from gui.main_window import MainWindow
from gui import cfg, plugins,  pics_rc
import sys

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # import is placed here because handler's dialog needs QApplication :
    import except_handler
    app.setApplicationName('Plume Creator')
    app.setApplicationVersion('1.5.0-alpha')
    app.setOrganizationDomain('http://www.plume-creator.eu')

    # app.setStyle(QStyleFactory.create("fusion"))
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53,53,53))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # palette.setColor(QPalette.Base, QColor(15,15,15))
    # palette.setColor(QPalette.AlternateBase, QColor(53,53,53))
    # palette.setColor(QPalette.ToolTipBase, Qt.white)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53,53,53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    # palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    # palette.setColor(QPalette.Highlight, QColor(142,45,197).lighter())
    # palette.setColor(QPalette.HighlightedText, Qt.black)
    # app.setPalette(palette)

    data = Data()
    cfg.data = data
    cfg.data_subscriber = subscriber
    cfg.gui_plugins = plugins.Plugins()

    window = MainWindow()
    arguments = sys.argv
    del arguments[0]
    window.set_application_arguments(arguments)  # load project
    window.show()

    sys.exit(app.exec_())
