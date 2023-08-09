import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(1000, 300, 500, 500)
        self.initUI()
        self.calculate()

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number1")
        self.lbl_number1.move(50, 30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150, 30)
        self.txt_number1.resize(200, 32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number2")
        self.lbl_number2.move(50, 80)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150, 80)
        self.txt_number2.resize(200, 32)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Addition")
        self.btn_add.move(150, 130)
        self.btn_add.clicked.connect(self.calculate)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("Subtraction")
        self.btn_sub.move(250, 130)
        self.btn_sub.clicked.connect(self.calculate)

        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText("Multiplication")
        self.btn_mul.move(150, 180)
        self.btn_mul.clicked.connect(self.calculate)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Division")
        self.btn_div.move(250, 180)
        self.btn_div.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result :")
        self.lbl_result.move(150, 230)


    def calculate(self):
        sender = self.sender()
        result = 0

        if sender.text() == "Addition":
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
        elif sender.text() == "Subtraction":
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
        elif sender.text() == "Multiplication":
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
        elif sender.text() == "Division":
            result = int(self.txt_number1.text()) / int(self.txt_number2.text())

        self.lbl_result.setText("Result : " + str(result))


def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()