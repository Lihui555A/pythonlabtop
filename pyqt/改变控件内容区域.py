import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        label=QLabel(self)
        label.resize(100,100)
        label.setText('hhhhhhhh')
        label.setStyleSheet('background-color:red')
        print(label.contentsRect())#查看标签控件的内容区域的大小
        label.setContentsMargins(30,30,30,30)#这句话的意思是设置标签控件中的能写文字的那一小块区域距离标签控件的左边，上面，右边，下边的距离
        print(label.contentsRect())#答应打印出来的前两个结果是修改后的标签中的能写文字的那一小块区域的左上角距离标签客户区域的左上角的距离，后边两个是这一小块内容区域的宽和高

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())