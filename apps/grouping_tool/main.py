from PyQt5.QtWidgets import QMainWindow
from .ui import Ui_MainWindow
from . import ui_function
from .ui_function import *


class GroupingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Grouping-Tool")

        self.connect_ui_with_event()
        combo_box_Initialize(self.ui)

    def connect_ui_with_event(self):
        '''
        Tab 1 : Kitting Tool
        '''
        self.ui.edgeSearchButton.clicked.connect(
            lambda: search_event(self.ui, 'edge'))
        self.ui.edgeComboBox.currentIndexChanged.connect(
            lambda _: edge_combo_changed_event(self.ui))

        self.ui.childSearchButton.clicked.connect(
            lambda: search_event(self.ui, 'child'))

        self.ui.bomComboBox.currentIndexChanged.connect(
            lambda _: bom_combobox_changed_event(self.ui))
        self.ui.bomRefreshButton.clicked.connect(
            lambda _: refresh_bom_event(self.ui))
        bom_combobox_changed_event(self.ui)

        self.ui.addGroupButton.clicked.connect(
            lambda: add_group_event(self.ui))

        '''
        Tab 2 : BOM Setting
        '''
        self.ui.addProfileButton.clicked.connect(
            lambda: add_profile_event(self.ui))
        self.ui.deleteRowButton.clicked.connect(
            lambda: delete_selected_row(self.ui.bomTableView))
        self.ui.addBomButton.clicked.connect(
            lambda: add_bom_event(self.ui))
        self.ui.clearBomButton.clicked.connect(
            lambda: clear_group_event(self.ui))
        refresh_bom_event(self.ui)


if __name__ == "__main__":
    pass
