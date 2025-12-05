from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QTimer
from funcoes import somar, subtrair, multiplicar, dividir, porcentagem
from os import path
import sys

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    return path.join(base_path, file)

class CalcUI(QMainWindow): 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi(loadFile("view/calculadora.ui"), self)
        self.show()

        self.num1 = 0
        self.num2 = 0
        self.finish = False

        self.selectedOperation = None
        
        self.operationList = {
            "+": somar,
            "-": subtrair,
            "x": multiplicar,
            "÷": dividir,
        }

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
        self.btn_virg.clicked.connect(self.virg)
        self.btn_clear.clicked.connect(self.cleanDisplay)
        self.btn_invert.clicked.connect(self.invert)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_apagar.clicked.connect(self.apagarDisplay)
        self.btn_mais.clicked.connect(lambda: self.setOperation("+"))
        self.btn_menos.clicked.connect(lambda: self.setOperation("-"))
        self.btn_divi.clicked.connect(lambda: self.setOperation("÷"))
        self.btn_vezes.clicked.connect(lambda: self.setOperation("x"))
        self.btn_porcen.clicked.connect(self.percent)

    def timerClean(self):

        self.btn_virg.setEnabled(False)
        self.btn_clear.setEnabled(False)
        self.btn_invert.setEnabled(False)
        self.btn_igual.setEnabled(False)
        self.btn_apagar.setEnabled(False)
        self.btn_mais.setEnabled(False)
        self.btn_menos.setEnabled(False)
        self.btn_divi.setEnabled(False)
        self.btn_vezes.setEnabled(False)
        self.btn_porcen.setEnabled(False)

        self.timer = QTimer(self)
        self.timer.singleShot(1000, self.timeOutClean)

    def timeOutClean(self):
        self.btn_virg.setEnabled(True)
        self.btn_clear.setEnabled(True)
        self.btn_invert.setEnabled(True)
        self.btn_igual.setEnabled(True)
        self.btn_apagar.setEnabled(True)
        self.btn_mais.setEnabled(True)
        self.btn_menos.setEnabled(True)
        self.btn_divi.setEnabled(True)
        self.btn_vezes.setEnabled(True)
        self.btn_porcen.setEnabled(True)
        self.display.setText("0")
        self.display2.setText("0")
        self.num1 = 0
        self.num2 = 0
        self.selectedOperation = None

    def addNumber(self, numero):
        last = self.display.text()
        if last == "0" or self.finish:
            self.finish = False
            self.display.setText(f"{numero}")
        else:    
            self.display.setText(last + f"{numero}")
    
    def cleanDisplay(self):
        self.display.setText("0")
        if self.display.text() == "0":
            self.display2.setText("0")

    def apagarDisplay(self):
        last = self.display.text()
        last = last[:-1]
        if len(last) == 0:
            last = "0"
        self.display.setText(last)

    def invert(self):
        numero = self.getNumberDisplay(self.display)
        x = str(numero * -1)
        self.setNumberDisplay(x)

    def percent(self):
        perc = self.getNumberDisplay(self.display)
        result = porcentagem(self.num1, perc)
        self.setNumberDisplay(result)

    def setOperation(self, operation):
        self.selectedOperation = operation
        self.num1 = self.getNumberDisplay(self.display)
        self.num2 = 0
        result = self.display.text()
        self.display2.setText(result)
        self.display.setText("0")
        self.btn_clear.setText("AC")

        
    def virg(self):    
        ultimo = self.display.text()
        if "," in ultimo:
            return
        else:
            result = ultimo + ","
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
        if self.selectedOperation:
            if self.num2 == 0:
                self.num2 = self.getNumberDisplay(self.display)
    
            num1 = self.num1
            num2 = self.num2
            operation = self.operationList.get(self.selectedOperation)
            result = operation(num1, num2)
            self.num1 = result
    
            self.setNumberDisplay(result)
            self.setCalcDisplay(num1, num2, self.selectedOperation)
            self.finish = True
            if isinstance(result, str):
                self.timerClean()