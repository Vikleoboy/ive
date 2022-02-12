from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("HOrney")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('what do u want ??')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("U feel Horney")
        self.b1.move(50, 90)
        self.b1.clicked.connect(self.clickedb1)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("i dont feel anything ")
        self.b2.move(50, 150)
        self.b2.clicked.connect(self.clickedb2)

    def clickedb1(self):
        self.label.setText('FUck your self ')
        self.update()

    def clickedb2(self):
        self.label.setText(' u are dead then')
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


window()
