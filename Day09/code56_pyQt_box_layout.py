import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton=QPushButton('OK')
        cancleButton=QPushButton('Cancel')

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancleButton)
        hbox.addStretch(1)

        vbox=QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)#addStretch로 아래 위 공간 3:1로 유지

        self.setLayout(vbox)

        self.setWindowTitle('박스 배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
