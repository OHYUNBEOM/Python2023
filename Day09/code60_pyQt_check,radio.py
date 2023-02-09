#레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb1=QCheckBox('CheckBox1',self)#다중선택 가능
        cb1.move(20,20)
        cb1.toggle()
        #signal
        cb1.stateChanged.connect(self.changeTitle)

        cb2=QCheckBox('CheckBox2',self)
        cb2.move(20,60)
        cb2.stateChanged.connect(self.changeCheck)

        rb1=QRadioButton('First Button',self)
        rb1.move(20,120)
        rb1.setChecked(True)

        rb2=QRadioButton('Second Button',self)#다중선택 불가
        rb2.move(20,160)

        self.setWindowTitle('Check,Radio Button')
        self.setGeometry(1000,300,300,300)
        self.show()


    def changeCheck(self,state):
        if state==Qt.CheckState.Checked:
            self.setWindowTitle('CbeckBox2 체크됨')
        else:
            self.setWindowTitle('CbeckBox2 체크됨')

    def changeTitle(self,state):#상태 변경될때
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('CheckBox1 체크됨')
        else:
            self.setWindowTitle('CheckBox1 체크해제')

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())