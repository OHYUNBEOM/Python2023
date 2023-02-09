import sys
from PyQt5.QtWidgets import QApplication,QWidget


class MyApp(QWidget):#MyApp class 생성, 부모:Qwidget
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출
    def initUI(self):

        self.setWindowTitle('App')#Form제목
        self.setGeometry(1000,300,500,250)#setGeometry(x,y,너비,높이)
        # self.move(1000,300)#(x,y)위치에 위젯 생성
        # self.resize(500,250)#(너비,높이) 위젯 생성
        self.show()#위젯 출력
if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())