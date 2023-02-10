import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button_dialog=QPushButton('Dialog',self)
        self.button_dialog.move(20,20)
        self.button_dialog.clicked.connect(self.onClicked)#signal(event)발생 시 onClicked 호출

        self.txtInput=QLineEdit(self)
        self.txtInput.move(20,50)

        self.setWindowTitle('Dialog')
        self.setGeometry(1000,300,300,300)
        self.show()

    def onClicked(self):
        text,ok=QInputDialog.getText(self,'Input Dialog','문자열 입력:')
        if ok:
            self.txtInput.setText(str(text))

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())