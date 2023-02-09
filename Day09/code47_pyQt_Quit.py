import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):#MyApp class 생성, 부모:Qwidget
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출
    def initUI(self):
        btn=QPushButton('Quit',self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)#종료

        self.setWindowTitle('Quit Button')
        self.setWindowIcon(QIcon('.\images\iot.png'))
        self.setGeometry(1000,300,500,250)
        
        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())