from apps.app1.main import App1Window
from apps.app2.main import App2Window
from apps.app3.main import App3Window
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
import sys


class SuperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SDE Super App")

        self.tab_widget = QTabWidget(self)
        self.tab_widget.currentChanged.connect(self.adjustWindowSize)

        self.app1 = App1Window()
        self.app2 = App2Window()
        self.app3 = App3Window()

        self.tab_widget.addTab(self.app1, "App 1")
        self.tab_widget.addTab(self.app2, "App 2")
        self.tab_widget.addTab(self.app3, "App 3")

        self.setCentralWidget(self.tab_widget)

        # Initialize the window size based on the largest content among all tabs
        self.adjustWindowSize()

    def adjustWindowSize(self):
        # Initialize the maximum size
        max_width = 0
        max_height = 0

        for index in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(index)
            if tab:
                max_width = max(max_width, tab.width())
                max_height = max(max_height, tab.height())

        self.resize(max_width, max_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperApp()
    window.show()
    sys.exit(app.exec_())
