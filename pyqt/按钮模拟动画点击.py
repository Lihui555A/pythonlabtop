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
        button1.clicked.connect(lambda :print('我是按钮一'))

        button2 = QPushButton(self)
        button2.move(200, 200)
        button2.setText('按钮二')
        button2.clicked.connect(self.start_button_1)

        button3 = QPushButton(self)
        button3.move(300, 300)
        button3.setText('按钮三')
        button3.clicked.connect(lambda :self.button1.animateClick(1000))#执行这句话也可以实现按钮一的模拟操作，只不过这种操作比上面那种操作能够看到按钮一的按下动作
        self.button1=button1
        self.button2=button2
        self.button3=button3
    def start_button_1(self):
        self.button1.click()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())