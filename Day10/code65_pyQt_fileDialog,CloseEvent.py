import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
 
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile=QAction(QIcon('iot.png'),'Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.onClicked)

        menubar=self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(1000,300,300,300)
        self.show()


    def onClicked(self):
            fname=QFileDialog.getOpenFileName(self,'Open file','./')#getOpenFileName메소드로 File선택

            if fname[0]:#파일을 선택했다면
                file = open(fname[0],'r',encoding='utf-8')
                with file:
                    data=file.read()
                    self.textEdit.setText(data)

                file.close()

            QMessageBox.about(self,'성공','로드했습니다') #로드 성공 메시지 출력

    def closeEvent(self, event):#closeEvent 재정의 
        reply = QMessageBox.question(self,'Message','종료됩니다. 종료하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#Yes or No / 기본 설정버튼 : NO
        if reply == QMessageBox.Yes: 
            event.accept()
        else:
            event.ignore()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())