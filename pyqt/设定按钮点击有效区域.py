import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        button1=pushbutton(self)
        button1.move(100,100)
        button1.setText('按钮一')
        button1.clicked.connect(lambda :print('我是按钮一'))
        button1.resize(200,200)
class pushbutton(QPushButton):
    def hitButton(self, pos):
        if pos.x()>self.width()/2:
            return True
        return False




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())