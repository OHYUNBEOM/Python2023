import sys
from PyQt5.QtWidgets import QApplication,QMainWindow


class MyApp(QMainWindow):#MyApp class,부모:QMainWindow StatusBar 사용하려면 QMainWindow 필요함
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Statusbar')
        self.setGeometry(1000,300,500,250)#setGeometry(x,y,너비,높이)
        self.show()#위젯 출력
if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())