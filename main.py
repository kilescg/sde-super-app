from apps.app1.main import App1Window
from apps.app2.main import App2Window
from apps.app3.main import App3Window
from apps.label_generator.main import LabelGenerator
from apps.grouping_tool.main import GroupingTool
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction
import sys


class SuperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SDE Super App")

        self.central_widget = None

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Apps")

        app1_action = QAction("App 1", self)
        app1_action.triggered.connect(lambda: self.show_app(App1Window()))
        file_menu.addAction(app1_action)

        app2_action = QAction("App 2", self)
        app2_action.triggered.connect(lambda: self.show_app(App2Window()))
        file_menu.addAction(app2_action)

        app3_action = QAction("App 3", self)
        app3_action.triggered.connect(lambda: self.show_app(App3Window()))
        file_menu.addAction(app3_action)

        label_generator_action = QAction("Label Generator", self)
        label_generator_action.triggered.connect(
            lambda: self.show_app(LabelGenerator()))
        file_menu.addAction(label_generator_action)

        grouping_tool_action = QAction("Label Generator", self)
        grouping_tool_action.triggered.connect(
            lambda: self.show_app(GroupingTool()))
        file_menu.addAction(grouping_tool_action)

        self.show_app(LabelGenerator())

    def show_app(self, app_widget):
        if self.central_widget:
            self.central_widget.hide()
            self.central_widget.setParent(None)

        self.central_widget = app_widget
        self.setCentralWidget(app_widget)
        self.resize(app_widget.size())
        app_widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperApp()
    window.show()
    sys.exit(app.exec_())
