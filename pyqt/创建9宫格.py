import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.num=20 #一共要放的按钮的个数
        self.width_num=3#每行要放的按钮的个数
        self.setup_ui()

    def setup_ui(self):
        for i in range(0,self.num):
            button=QPushButton(self)
            button.resize(self.width()/self.width_num,self.height()/(self.num//self.width_num+1))#self.num//self.width_num+1)列数
            print(i//self.width_num,i%(self.num//self.width_num+1))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())

