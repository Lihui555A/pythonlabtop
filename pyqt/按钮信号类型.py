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
        button1.pressed.connect(lambda :print('鼠标被按下'))#鼠标被按下时发射信号
        button1.released.connect(lambda :print('鼠标被释放'))#鼠标在按钮控件范围内释放，或者鼠标移出按钮范围触发信号
        button1.clicked.connect(lambda :print('鼠标被点击'))#鼠标在按钮上按下加释放后发射这个信号
        button1.toggled.connect(lambda :print('按钮状态切换了')) #这个函数要执行的话必须把按钮的可选中状态设置为能够选中，然后点击按钮后会改变选中状态，然后发射这个信号从而引发函数响应

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())