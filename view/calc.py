from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import soma

class CalcUI(QMainWindow): 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/calculadora.ui", self)
        self.show()

        # QShortcut(QKeySequence("0"), self).activated.connect(lambda: self.addNumber(0))
        self.btn_1.clicked.connect(lambda: self.addNumber(1))
        self.btn_2.clicked.connect(lambda: self.addNumber(2))
        self.btn_3.clicked.connect(lambda: self.addNumber(3))
        self.btn_4.clicked.connect(lambda: self.addNumber(4))
        self.btn_5.clicked.connect(lambda: self.addNumber(5))
        self.btn_6.clicked.connect(lambda: self.addNumber(6))
        self.btn_7.clicked.connect(lambda: self.addNumber(7))
        self.btn_8.clicked.connect(lambda: self.addNumber(8))
        self.btn_9.clicked.connect(lambda: self.addNumber(9))
        self.btn_0.clicked.connect(lambda: self.addNumber(0))
        self.btn_mais.clicked.connect(lambda: self.addNumber("+"))
        self.btn_menos.clicked.connect(lambda: self.addNumber("-"))
        self.btn_divi.clicked.connect(lambda: self.addNumber("÷"))
        self.btn_vezes.clicked.connect(lambda: self.addNumber("x"))
        self.btn_virg.clicked.connect(self.virg)
        self.btn_porcen.clicked.connect(lambda: self.addNumber("%"))
        self.btn_clear.clicked.connect(self.cleanDisplay)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_apagar.clicked.connect(self.apagarDisplay)


    def addNumber(self, numero):
        last = self.display.text()
        if last == "0":
            self.display.setText(f"{numero}")
        else:    
            self.display.setText(last + f"{numero}")
    
    def cleanDisplay(self):
        self.display.setText("0")

    def apagarDisplay(self):
        last = self.display.text()
        self.display.setText(last[:-1])

    def showResult(self):
        num1 = self.display.text()
        if "," in num1:
            num1 = num1.repalce(",", ".")
            num1 = float(num1)
        else:
            num1 = int(num1)

        num2 = 2    
        result = soma(num1, num2)
        print(f"Número: {result}")

    def virg(self):
        last = self.display.text()
        if last.count(",") > 0:
            result = last
        result = last + ","
        self.display.setText(result) 
    