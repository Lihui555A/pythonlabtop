import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget,QIcon
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        button1=QPushButton(self)
        button1.setText('我是按钮一')
        button1.move(100,100)
        button2=QPushButton('我是按钮二',self)
        button2.move(200,200)
        button2 = QPushButton(QIcon(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\noshadow\standart\bmp\24x24\001_03.bmp'),'我是按钮三', self)
        button2.move(300, 300)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())