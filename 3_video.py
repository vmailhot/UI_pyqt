import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("My first app")
        self.setToolTip("This is my app")
        self.setWindowIcon(QIcon("gorrila.jpeg"))
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Name: ")
        self.lbl_name.move(50, 50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname: ")
        self.lbl_surname.move(50, 90)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200, 50)
        self.txt_name.resize(200, 32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200, 90)
        self.txt_surname.resize(200, 32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200, 130)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(200, 170)
        self.lbl_result.resize(200, 200)

    
    def clicked(self):
        self.lbl_result.setText("Name\t:" + self.txt_name.text() + "\nSurname\t:" + self.txt_surname.text())




def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())


window()
