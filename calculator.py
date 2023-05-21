import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        #оси выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_result)

        #виджеты и их привязка к осям
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_multiply = QPushButton("×", self)
        self.hbox_third.addWidget(self.b_multiply)

        self.b_point = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_point)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_clear = QPushButton("clear", self)
        self.hbox_fourth.addWidget(self.b_clear)

        self.b_division = QPushButton("÷", self)
        self.hbox_fourth.addWidget(self.b_division)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        #штучка дрючка
        self._clear()

        #события, отвечающие за реакции на нажатия по кнопкам
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("×"))
        self.b_division.clicked.connect(lambda: self._operation("÷"))
        self.b_point.clicked.connect(self._point)
        self.b_result.clicked.connect(self._result)
        self.b_clear.clicked.connect(self._clear)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    #метод класса для обработки кнопок с цифрами
    def _button(self, param):
        line = self.input.text()
        if self._check_float(line) or self._check_int(line) or line == "":
            self.input.setText(line + param)

    #метод класса для обработки кнопок с математическими операциями
    def _operation(self, op):
        if self._check_float(self.input.text()):
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")

    #метод класса для обработки кнопки плавающей точки
    def _point(self):
        if self._check_int(self.input.text()):
            self.input.setText(str(self.input.text()) + ".")

    #метод класса для обработки кнопки результата
    def _result(self):
        self.num_2 = self.input.text()
        if self._check_float(self.num_1) and self._check_float(self.num_2):
            self.num_2 = float(self.num_2)
            if self.op == "+":
                res = self.num_1 + self.num_2
            elif self.op == "-":
                res = self.num_1 - self.num_2
            elif self.op == "×":
                res = self.num_1 * self.num_2
            elif self.op == "÷":
                if self.num_2 == 0.0:
                    res = "error"
                else:
                    res = self.num_1 / self.num_2

            if self._check_float(res):
                if int(res) == float(res):
                    res = int(res)
                self.num_1 = res
            else:
                self.num_1 = ""
            self.input.setText(str(res))

    #метод класса для обработки кнопки очистки
    def _clear(self):
        self.num_1 = ""
        self.num_2 = ""
        self.input.setText("")

    #метод класса для проверки значения
    def _check_float(self, value):
        try:
            float(value)
            return True
        except:
            return False

    def _check_int(self, value):
        try:
            int(value)
            return True
        except:
            return False


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
