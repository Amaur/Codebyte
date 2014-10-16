from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class App(QWidget):
    """docstring for App"""
    def __init__(self, parent=None):
        super(App, self).__init__()
        self.settings_window()
        self.hello = QLabel("Slt, vous..!", self)
    def settings_window(self):
        self.resize(700,400)
        self.setWindowTitle("Hello world")



if __name__ == '__main__':
    root =QApplication([])
    app =App()
    app.show()
    sys.exit(root.exec_())



