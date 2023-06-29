from PyQt5.QtWidgets import *
from PyQt5 import uic

# creates a class to import QT designer UI
class MyGUI(QMainWindow):
    def __init__(self):

        # loads QT desinger file
        super(MyGUI, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()

        self.currentNum = ""

        button_List = self.findChildren(QPushButton)

        for button in button_List:
            if button.text() != "=":
                button.clicked.connect(lambda checked, btn=button: self.input(btn.text()))
            else:
                self.Btn_sum.clicked.connect(self.total)



    # outputs a message box containing a users input
    def input(self, num):
        
        # NEED TO DISPLAY MUTITPLE OPERATOR INPUT
        self.currentNum = self.currentNum + num

    def total(self):
        test = self.currentNum
        res = eval(test)
        print(res)



 

# main application
def main():
    # intinalises window
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()