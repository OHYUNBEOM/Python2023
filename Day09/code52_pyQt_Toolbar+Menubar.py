import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):#MyApp class,부모:QMainWindow / StatusBar 사용하려면 QMainWindow 필요함
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출

    def initUI(self):
        exitAction = QAction(QIcon('.\images\exit.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        testicon=QAction(QIcon('.\images\iot.png'),'iot',self)

        self.toolbar = self.addToolBar('Tooolbar') #마우스 올리면 Exit나옴
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(testicon)


        menubar=self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar+Toolbar')
        #self.setGeometry(1000,300,500,250)
        self.setcenter()#중심정렬
        self.show()
    
    # 화면 중심 셋팅
    def setcenter(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())