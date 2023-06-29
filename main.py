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
                self.Btn_sum



    # outputs a message box containing a users input
    def input(self, num):
        self.currentNum = self.currentNum + num
        print(self.currentNum)
 

# main application
def main():
    # intinalises window
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()