from PyQt5.QtWidgets import QMainWindow
from .ui import Ui_MainWindow


class LabelGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Label-Generator")


if __name__ == "__main__":
    pass
