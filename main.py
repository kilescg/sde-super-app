from apps.template_app.main import TemplateWindow
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

        label_generator_action = QAction("Label Generator", self)
        label_generator_action.triggered.connect(
            lambda: self.show_app(LabelGenerator()))
        file_menu.addAction(label_generator_action)

        grouping_tool_action = QAction("Grouping Tool", self)
        grouping_tool_action.triggered.connect(
            lambda: self.show_app(GroupingTool()))
        file_menu.addAction(grouping_tool_action)

        template_action = QAction("Template UI", self)
        template_action.triggered.connect(
            lambda: self.show_app(TemplateWindow()))
        file_menu.addAction(template_action)

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
