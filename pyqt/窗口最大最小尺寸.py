import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        #self.setFixedSize(100,100)#固定尺寸不能再变化了
        self.setMinimumSize(200,200)
        self.setMaximumSize(600,600)
        self.resize(800,800)#resize这个时候就不好使了

        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())