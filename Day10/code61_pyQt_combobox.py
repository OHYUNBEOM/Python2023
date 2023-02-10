import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1=QLabel('option1',self)#self. 으로 변수 선언 시 내 class인 MyApp 전체에서 Label1이란 변수 사용하고자 할 때.
        self.label1.move(50,150)#하단에 라벨 생성

        cb=QComboBox(self)
        cb.addItem('option1')
        cb.addItem('option2')
        cb.addItem('option3')
        cb.addItem('option4')
        cb.move(50,50)#50,50위치에 option1,2,3,4를 항목으로 가진 comboBox생성
        #Signal 발생시 (Signal=사용자 검색따위가 발생시) 
        cb.activated[str].connect(self.onActivated)#콤보박스 옵션 선택시 onActivated 호출
        
        self.setWindowTitle('콤보박스')
        self.setGeometry(1000,300,300,300)
        self.show()

    def onActivated(self,text):
        self.label1.setText(text+' 선택')#콤보박스 선택 시 라벨에 콤보박스 text 나오게
        self.label1.adjustSize()#크기 자동조절
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())