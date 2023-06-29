from PyQt5.QtWidgets import *
from PyQt5 import uic

# creates a class to import QT designer UI
class MyGUI(QMainWindow):
    def __init__(self):

        # loads QT desinger file
        super(MyGUI, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()

        self.currentExp = ""

        button_List = self.findChildren(QPushButton)
        self.num_Buttons = []
        self.operator_Buttons = []

        for button in button_List:
            if button.text() == "=":
                button.clicked.connect(self.total)
                self.operator_Buttons.append(button)
            elif button.text() == "C":
                button.clicked.connect(self.clear)
            else:
                button.clicked.connect(lambda checked, btn=button: self.input(btn.text()))

                if button.text().isdigit():
                    self.num_Buttons.append(button)
                else:
                    self.operator_Buttons.append(button)                


    # outputs a message box containing a users input
    def input(self, userInput):
        
        if len(self.currentExp) > 0:

            # prevents division by zero
            if self.currentExp[-1] != "/":
                self.Btn_0.setEnabled(True)

            # Prevents user from inputting two operators consecutively
            if not (self.currentExp[-1].isdigit() or userInput.isdigit()):
                return

            # adds current input to expression
            self.currentExp += userInput
            self.outputLbl.setText(self.currentExp)

            # prevents division by zero
            if userInput == "/":
                self.Btn_0.setEnabled(False)

        # checks if first input is an operator        
        elif userInput.isdigit():

            # adds input tp expression
            self.currentExp += userInput
            self.outputLbl.setText(self.currentExp)

    # sums up total
    def total(self):
        res = eval(self.currentExp)
        self.outputLbl.setText(self.currentExp + "=" + str(res))
        self.currentExp = str(res)

    # clears 
    def clear(self):
        self.Btn_0.setEnabled(True)
        self.currentExp = ""
        self.outputLbl.setText("")



 

# main application
def main():
    # intinalises window
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()