import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        grid=QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'),0,0) #row,col=0,0
        grid.addWidget(QLabel('Title'),1,0) #1행 0열
        grid.addWidget(QLabel('Title'),2,0) #2행 0열 

        grid.addWidget(QLineEdit(),0,1) #0행 1열
        grid.addWidget(QLineEdit(),1,1) #1행 1열
        grid.addWidget(QTextEdit(),2,1) #2행 1열

        okButton=QPushButton('OK') #버튼도 추가해보자
        cancleButton=QPushButton('Cancel')
        grid.addWidget(okButton,3,1) #3행 1열
        grid.addWidget(cancleButton,4,1) #4행 1열
        

        self.setWindowTitle('그리드 배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())