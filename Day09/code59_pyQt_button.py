import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button1=QPushButton('Button&1',self)#&Button으로 선언하여 Alt+B로 버튼 활성화 가능(단축키st)
        button1.setCheckable(True)#선택(체크)상태
        button1.toggle()#toggle 호출 해야 시작과 동시에 버튼선택된 상태로 나옴

        button2=QPushButton('Button&2',self)#버튼선택 단축키 &2
        button2.setCheckable(True)
        button2.toggle()

        button3=QPushButton('Button3',self)#버튼선택 단축키 &2
        button3.setEnabled(False)#버튼 비활성화

        vbox=QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        self.setLayout(vbox)

        self.setWindowTitle('버튼')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())