#레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1=QLabel('Label1',self)
        label1.move(20,20)
        label2=QLabel('Label2',self)
        label2.move(20,60)
        
        button1=QPushButton('Button1',self)
        button1.move(80,13)
        button2=QPushButton('Button2',self)
        button2.move(80,53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300,300,300,300)
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
