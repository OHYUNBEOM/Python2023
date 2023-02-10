import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1=QLabel(self)
        self.label1.move(60,40)#해당 위치에 빈 라벨 생성

        qline=QLineEdit(self)#QLineEdit 위젯 생성
        qline.move(60,100)
        qline.textChanged[str].connect(self.onChanged)#qline텍스트 바뀌면 onchanged 호출

        self.setWindowTitle('LineEdit')
        self.setGeometry(1000,300,300,300)
        self.show()

    def onChanged(self,text):#text바뀌면 onChanged호출
        self.label1.setText(text)#qline 바뀔때마다 label에 해당 텍스트 뿌려줌
        self.label1.adjustSize()
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())