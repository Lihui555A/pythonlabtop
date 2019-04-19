import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        button1=QPushButton(self)
        button1.move(100,100)
        button1.setText('按钮一')
        button1.setAutoExclusive(True)
        button1.setCheckable(True)
        button2 = QPushButton(self)
        button2.move(200, 200)
        button2.setText('按钮二')
        button2.setCheckable(True)
        button2.setAutoExclusive(True) #设定按钮的排他新，默认是没有的，前提是得设定按钮的能够选中的功能
        button3 = QPushButton(self)
        button3.move(300, 300)
        button3.setText('按钮三')
        button3.setAutoExclusive(True)
        button3.setCheckable(True)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())