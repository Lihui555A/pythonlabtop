from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
import sys
class Winform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('关闭窗口的例子')
        self.button_1=QPushButton('关闭主窗口')
        self.button_1.clicked.connect(self.onbuttonclick)

        self.layout=QHBoxLayout()
        self.layout.addWidget(self.button_1)
        self.main_frame=QWidget()
        self.main_frame.setLayout(self.layout)
        self.setCentralWidget(self.main_frame)

    def onbuttonclick(self):
        sender=self.sender()  #self.sender()也是父类主窗口的一个方法，返回一个小字典吧应该是
        print(sender.text()+'被按下了')
        qapp=QApplication.instance()
        qapp.quit()
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=Winform()
    form.show()
    sys.exit(app.exec_())