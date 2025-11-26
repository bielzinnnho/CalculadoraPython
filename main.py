from PyQt5.QtWidgets import QApplication
from  view.calc import CalcUI

if __name__ == "__main__":
    app = QApplication([])
    tela = CalcUI()
    app.exec()