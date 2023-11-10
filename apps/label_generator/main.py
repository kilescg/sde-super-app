from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from .ui import Ui_MainWindow
from .ui_funciton import *


class LabelGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Label-Generator")

        self.connect_ui_with_event()
        self.SetTableHeader()
        self.ComboBoxInitialize()

    def connect_ui_with_event(self):
        self.ui.powerOnButton.clicked.connect(lambda: power_on_event())
        self.ui.powerOffButton.clicked.connect(lambda: power_off_event())
        self.ui.flashButton.clicked.connect(
            lambda: flash_event(self.ui))  # done

        self.ui.addGoodDeviceButton.clicked.connect(
            lambda: add_good_device_event(self.ui))
        self.ui.addBadDeviceButton.clicked.connect(
            lambda: add_bad_device_event(self.ui))
        self.ui.printNowButton.clicked.connect(
            lambda: print_now_event(self.ui))
        self.ui.clearListButton.clicked.connect(
            lambda: clear_list_event(self.ui))

    def ComboBoxInitialize(self):
        program_combobox_click_event(self.ui)

    def SetTableHeader(self):
        populate_table_view(self.ui.devicesTableView, header, [])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_G:
            add_good_device_event(self.ui)
        elif event.key() == Qt.Key_B:
            add_bad_device_event(self.ui)
        elif event.key() == Qt.Key_F:
            flash_event(self.ui)
        elif event.key() == Qt.Key_C:
            clear_list_event(self.ui)
        elif event.key() == Qt.Key_P:
            print_now_event(self.ui)
        elif event.key() == Qt.Key_Q:
            power_on_event(self.ui)
        elif event.key() == Qt.Key_W:
            power_off_event(self.ui)


if __name__ == "__main__":
    pass
