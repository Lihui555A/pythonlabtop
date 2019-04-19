#QObject类中有两个自身带的信号一个是obj.destroyed()
import sys
from PyQt5.Qt import QApplication,QWidget,QObject,QPushButton,QLabel
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        button=QPushButton(self)
        self.lable=QLabel(self)
        button.setText('点我')
        button.move(100,100)
        self.lable.setText('我要改变')
        button.clicked.connect(self.click_event)
    def click_event(self):
        self.lable.setText('我变了')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
