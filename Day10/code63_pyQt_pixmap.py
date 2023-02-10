import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap=QPixmap('./images/cat.png')

        label_image=QLabel()
        label_image.setPixmap(pixmap)
        label_size=QLabel(str(pixmap.width())+'x'+str(pixmap.height()))
        label_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox=QVBoxLayout(self)
        vbox.addWidget(label_image)
        vbox.addWidget(label_size)

        self.setLayout(vbox)

        self.setWindowTitle('LineEdit')
        self.setGeometry(1000,300,300,300)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())