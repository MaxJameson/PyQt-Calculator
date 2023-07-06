from PyQt5.QtWidgets import *
from PyQt5 import uic

# creates a class to import QT designer UI
class MyGUI(QMainWindow):
    def __init__(self):

        # loads QT desinger file
        super(MyGUI, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()

        # stores current expression
        self.currentExp = ""

        # stores the last input operator
        self.previousOp = ""

        # stores list of all buttons on the UI
        button_List = self.findChildren(QPushButton)

        # loops through buttons
        for button in button_List:

            # check the type of button
            match button.text():

                case "=":
                    # sets up = button
                    button.clicked.connect(self.total)

                case "C":
                    # sets up clear button
                    button.clicked.connect(self.clear)

                case "Back":
                    # Removes last input
                    button.clicked.connect(self.back)

                case _:
                    # sets up operators and number buttons
                    button.clicked.connect(lambda checked, btn=button: self.input(btn.text()))

              
    # outputs a message box containing a users input
    def input(self, userInput):

        self.Btn_Back.setEnabled(True)
        if len(self.currentExp) > 0:


            # Prevents user from inputting two operators consecutively
            if not (self.currentExp[-1].isdigit() or userInput.isdigit()):
                return
            # prevent multiple decimal points from being added to the same number
            elif (self.previousOp == "." and userInput == "."):
                return

            # adds current input to expression
            self.currentExp += userInput
            self.outputLbl.setText(self.currentExp)

            # checks if the current input is an operator and stores is
            if not(userInput.isdigit()):
                self.previousOp = userInput
            

            # prevents division by zero
            if userInput == "/":
                self.Btn_0.setEnabled(False)
            else:
                self.Btn_0.setEnabled(True)

        # checks if first input is an operator        
        elif userInput.isdigit():

            # adds input tp expression
            self.currentExp += userInput
            self.outputLbl.setText(self.currentExp)
            self.previousOp = userInput

    # sums up total
    def total(self):
        self.Btn_Back.setEnabled(False)
        res = eval(self.currentExp)
        self.outputLbl.setText(self.currentExp + "=" + str(res))
        self.currentExp = str(res)

    # clears expression
    def clear(self):
        self.Btn_Back.setEnabled(False)
        self.Btn_0.setEnabled(True)
        self.currentExp = ""
        self.outputLbl.setText("")

    # removes last input
    def back(self):
        
        # checks if an expression exists
        if len(self.currentExp) > 0:

            # removes last input
            self.currentExp = self.currentExp[:-1]
            self.outputLbl.setText(self.currentExp)

            # prevents divison by zero
            if len(self.currentExp) > 0 and self.currentExp[-1] != "/":
                self.Btn_0.setEnabled(True)
            elif len(self.currentExp) > 0 and self.currentExp[-1] == "/":
                self.Btn_0.setEnabled(False)



 

# main application
def main():

    
    # intinalises window
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()