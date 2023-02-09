import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):#MyApp class,부모:QMainWindow / StatusBar 사용하려면 QMainWindow 필요함
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출

    def initUI(self):
        exitAction = QAction(QIcon('.\images\exit.png'),'Exit',self)#아이콘,Exit라벨을 갖는 동작을 만든것
        exitAction.setShortcut('Ctrl+Q')#위 동작의 단축키를 Ctrl+Q로 정의
        exitAction.setStatusTip('Exit application')#라벨에 마우스 올렸을 때 상태바에 Exit application 출력
        exitAction.triggered.connect(qApp.quit)#내가만든 exitAction동작 선택 시 quit()메서드에 연결되면서 종료

        self.statusBar()#상태바(위젯 하단)

        menubar=self.menuBar()#메뉴바생성
        menubar.setNativeMenuBar(False)
        filemenu=menubar.addMenu('&File')#File메뉴 만드는데 &File로 만들면 해당 메뉴 단축키가 Alt+F가 됨.
        filemenu.addAction(exitAction)#File메뉴에 exitAction 동작 추가

        self.setWindowTitle('Menubar')
        self.setGeometry(1000,300,500,250)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())