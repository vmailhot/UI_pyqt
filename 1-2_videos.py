import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Size of the window and positon
    win.setGeometry(1200, 300, 700, 700)
    # Title of the window
    win.setWindowTitle("PyQt5 GUI")
    # Icon of the window
    win.setWindowIcon(QIcon('gorrila.jpeg'))
    win.setToolTip("My first GUI")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Enter your name :")
    lbl_name.move(50, 50)
    lbl_name.adjustSize()

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Enter your surname :")
    lbl_surname.move(50, 90)
    lbl_surname.adjustSize()

    # Textbox
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200, 50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200, 90)

    # Function to print the information in the console
    def clicked(self):
        print("button clicked")
        print("name :", txt_name.text())
        print("surname :", txt_surname.text())

    # When the button is pressed, the function clicked is called
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.clicked.connect(clicked)
    btn_save.move(200, 130)

    win.show()
    sys.exit(app.exec_())



window()