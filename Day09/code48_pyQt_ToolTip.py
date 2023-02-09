import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QIcon,QFont


class MyApp(QWidget):#MyApp class 생성, 부모:Qwidget
    def __init__(self):
        super().__init__()
        self.initUI()#생성자 생성과 동시에 initUI 호출
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')#self에 ToolTip찍으니까 widget에

        btn=QPushButton('ToolTipEx',self)#버튼생성
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50,50)#위치
        btn.resize(btn.sizeHint())

        self.setWindowTitle('ToolTip')
        self.setWindowIcon(QIcon('.\images\iot.png'))
        self.setGeometry(1000,300,500,250)

        self.show()
if __name__=='__main__':
    app=QApplication(sys.argv)#Application 객체 생성
    ex=MyApp()
    sys.exit(app.exec_())