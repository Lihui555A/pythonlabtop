from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton,qApp
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        label_1=QLabel(self)
        label_1.setText('我是第一个标签')
        label_1.move(100,200)
        label_1.setObjectName('label_1')
        label_2=QLabel(self)
        label_2.setText('我是第二个标签')
        label_2.move(200,300)
        label_2.setObjectName('label_2')
        label_3=QLabel(self)
        label_3.setText('我是第三个标签')
        label_3.move(250,250)
        label_3.setObjectName("label_3")
        button=QPushButton(self)
        button.setText('我是按钮')

        self.label_qss()
        self.find_children()
    def label_qss(self):
        with open('label.qss','r')as f:
            qApp.setStyleSheet(f.read())
    def find_children(self):
        print(self.findChildren(QLabel))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())