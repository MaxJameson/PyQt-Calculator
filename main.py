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

        # stores the operators in use
        self.ops = []

        # stores number of left and right brackets
        self.numLeftB = 0
        self.numRightB = 0

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

                # add brackets to sum
                case "(":
                    button.clicked.connect(self.bracket_left)
                
                case ")":
                    button.clicked.connect(self.bracket_right)

                case _:
                    # sets up operators and number buttons
                    button.clicked.connect(lambda checked, btn=button: self.input(btn.text()))

              
    # outputs a message box containing a users input
    def input(self, userInput):

        self.Btn_Back.setEnabled(True)
        if len(self.currentExp) > 0:


            # Prevents user from inputting two operators consecutively
            if not (self.currentExp[-1].isdigit() or userInput.isdigit()) and self.currentExp[-1] != ")":
                return
            # prevent multiple decimal points from being added to the same number
            elif(self.ops and userInput == "." and self.ops[-1] == "."):
                return

            # adds current input to expression
            self.currentExp += userInput
            self.outputLbl.setText(self.currentExp)

            # checks if the current input is an operator and stores is
            if not(userInput.isdigit()):
                self.ops.append(userInput)
            

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

    # sums up total
    def total(self):
        
        # checks expression has correct number of brackets
        if self.numLeftB > self.numRightB:
            missingBrackets = self.numLeftB - self.numRightB

            # inserts missing brackets
            for i in range(missingBrackets):
                self.currentExp += ")"
                self.outputLbl.setText(self.currentExp)

        # calculates and outputs sum
        res = eval(self.currentExp)
        self.outputLbl.setText(self.currentExp + "=" + str(res))

        # resets calculator
        self.currentExp = str(res)
        self.Btn_Back.setEnabled(False)
        self.numLeftB = 0
        self.numRightB = 0
        self.ops[0]

    # clears expression
    def clear(self):
        self.Btn_Back.setEnabled(False)
        self.Btn_0.setEnabled(True)
        self.currentExp = ""
        self.ops = []
        self.outputLbl.setText("")
        self.numLeftB = 0
        self.numRightB = 0

    # removes last input
    def back(self):
        
        # checks if an expression exists
        if len(self.currentExp) > 0:
            
            # check if item to delete is an operator
            if not(self.currentExp[-1].isdigit()):
                
                # check if item is a bracket and handles bracket managers
                if self.currentExp[-1] == "(":
                    self.numLeftB -= 1
                elif self.currentExp[-1] == ")":
                    self.numRightB -= 1
                
                # removes operator from list
                self.ops.pop()

            # removes last input
            self.currentExp = self.currentExp[:-1]
            self.outputLbl.setText(self.currentExp)

            # prevents divison by zero
            if len(self.currentExp) > 0 and self.currentExp[-1] != "/":
                self.Btn_0.setEnabled(True)
            elif len(self.currentExp) > 0 and self.currentExp[-1] == "/":
                self.Btn_0.setEnabled(False)


    # adds a left bracket to the expression
    def bracket_left(self):

        # check is a bracket is being input next to a number and adds multiplication
        if len(self.currentExp) > 0 and (self.currentExp[-1].isdigit() or self.currentExp[-1] == "."):
            self.currentExp += "*"
            self.outputLbl.setText(self.currentExp)

        # adds left bracket and updates bracket counter and operator list
        self.currentExp += "("
        self.outputLbl.setText(self.currentExp)
        self.numLeftB += 1
        self.ops.append("(")

   
            
    # adds a right bracket to the expression
    def bracket_right(self):

        # checks if the right amount of left brackets exists, then adds a right bracket
        if self.numLeftB > self.numRightB and self.currentExp[-1].isdigit():
            self.currentExp += ")"
            self.outputLbl.setText(self.currentExp)
            self.numRightB += 1
            self.ops.append(")")
            print("left: ", self.numLeftB, " right: ", self.numRightB)



# main application
def main():
    
    # intinalises window
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()