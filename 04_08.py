import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 200)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon.png"))

        btn = QPushButton("button1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

        btn2 = QPushButton("button2", self)
        btn2.move(10, 40)
        btn2.clicked.connect(self.btn2_clicked)

        btn3 = QPushButton("button3", self)
        btn3.move(10, 70)
        btn3.clicked.connect(self.btn3_clicked)


    def btn_clicked(self):
        print("button1 clicked!")



    def btn2_clicked(self):
        print("button2 clicked!")

    def btn3_clicked(self):
        print("button3 clicked!")


app = QApplication(sys.argv)
window = TestWindow()
window.show()
app.exec_()

