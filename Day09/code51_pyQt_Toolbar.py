import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):#MyApp class,부모:QMainWindow
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('.\images\exit.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)#종료하는 동작 추가

        self.statusBar()
        
        self.toolbar = self.addToolBar('Exit') #마우스 올리면 Exit나옴
        self.toolbar.addAction(exitAction)#위에 설정한 exitAction을 toolbar에 뿌려줌

        self.setWindowTitle('Toolbar')
        self.setGeometry(1000,300,500,250)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())