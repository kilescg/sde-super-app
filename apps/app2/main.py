from PyQt5.QtWidgets import QMainWindow, QLabel


class App2Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App 2")

        label = QLabel("This is App 2", self)


# This part is only executed when app2 is run as a standalone application
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = App2Window()
    window.show()
    sys.exit(app.exec_())
