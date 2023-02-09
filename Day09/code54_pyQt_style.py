import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #스타일
        label1=QLabel('Red')
        label2=QLabel('Green')
        label3=QLabel('Blue')

        label1.setStyleSheet("color:red;"#글자색
                            "border-style:solid;"#경계선:실선
                            "border-width:4px;"#경계선두께
                            "border-color:#FA8072;"#경계선색
                            "border-radius:3px")#경계선모서리
        label2.setStyleSheet("color:green;"
                            "background-color:#7FFFD4")#배경색
        label3.setStyleSheet("color:blue;"
                            "border-style:dashed;"
                            "border-width:4px;"
                            "border-color:#1E90FF")

        vbox=QVBoxLayout()#VBox : 가로로 출력 / HBox : 세로로 출력
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)

        self.setLayout(vbox)

        self.setWindowTitle('stylesheet')
        self.setGeometry(1000,300,300,300)
        self.show()
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())