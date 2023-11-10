from PyQt5.QtWidgets import QMainWindow
from .ui import Ui_MainWindow


class GroupingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Grouping-Tool")


if __name__ == "__main__":
    pass
