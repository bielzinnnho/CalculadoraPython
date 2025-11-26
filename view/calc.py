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
        # self.btn_mais.clicked.connect(lambda: self.addNumber("+"))
        # self.btn_menos.clicked.connect(lambda: self.addNumber("-"))
        # self.btn_divi.clicked.connect(lambda: self.addNumber("÷"))
        # self.btn_vezes.clicked.connect(lambda: self.addNumber("x"))
        self.btn_virg.clicked.connect(self.virg)
        self.btn_porcen.clicked.connect(lambda: self.addNumber("%"))
        self.btn_clear.clicked.connect(self.cleanDisplay)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_apagar.clicked.connect(self.apagarDisplay)
        self.btn_mais.clicked.connect(self.setOperation)
        self.btn_menos.clicked.connect(self.setOperation)
        self.btn_divi.clicked.connect(self.setOperation)
        self.btn_vezes.clicked.connect(self.setOperation)


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
        last = last[:-1]
        if len(last) == 0:
            last = "0"
        self.display.setText(last)

    def setOperation(self):
        result = self.display.text()
        self.display2.setText(result)
        self.cleanDisplay()
        


    def virg(self):
        last = self.display.text()
        if last.count(",") > 0:
            result = last
        result = last + ","
        self.display.setText(result) 
    
    def getNumberDisplay(self, display):
        num = display.text()
        if "," in num:
            num = num.replace(",", ".")
            num = float(num)
        else:
            num = int(num)
        return num
    
    def setNumberDisplay(self, num):
        num = str(num)
        num = num.replace("." , ",")
        self.display.setText(num)

    def setCalcDisplay(self, num1, num2, operation):
        num1 = str(num1).replace(".", ",")
        num2 = str(num2).replace(".", ",")
        result = f"{num1} {operation} {num2} = "
        self.display2.setText(result)

    def showResult(self):
        num1 = self.getNumberDisplay(self.display)
        num2 = self.getNumberDisplay(self.display2)
        result = soma(num1, num2)
        self.setNumberDisplay(result)