import sys
from PyQt5.QtWidgets import QApplication,QWidget
from 一个标签用的链接一个按钮用的资源文件 import Ui_Form #这里的导包可以不从大的文件夹下调用
class MyMainWindow(QWidget,Ui_Form):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)#这个括号里填的self是指的新建的类中的QMainWindow,因为原来的Ui_MainWindow中的setupUi()函数中需要加一个主窗体
        self.label_2.linkHovered.connect(self.printtext)
    def printtext(self):
        print('hhahahah')
if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())