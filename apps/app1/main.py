from PyQt5.QtWidgets import QMainWindow, QPushButton


class App1Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App 1")

        button = QPushButton("Click Me", self)
        button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        # Perform app-specific actions
        print("Button in App 1 clicked!")


# This part is only executed when app1 is run as a standalone application
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = App1Window()
    window.show()
    sys.exit(app.exec_())
