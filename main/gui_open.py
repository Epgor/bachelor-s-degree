import sys


from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox

)

from PyQt5.uic import loadUi


from window import Ui_ZubrSecurityMainWidnow


class Window(QMainWindow, Ui_ZubrSecurityMainWidnow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setupUi(self)




if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec())