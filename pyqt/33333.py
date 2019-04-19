import sys,cv2
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from pyqt.a import Ui_Form
class MyMainWindow(QWidget,Ui_Form):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)#这个括号里填的self是指的新建的类中的QMainWindow,因为原来的Ui_MainWindow中的setupUi()函数中需要加一个主窗体
        self.pushButton.clicked.connect(self.openMsg)

    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,'打开','C:/','All Files(*);;Text Files(*.txt)')
        image=cv2.imread(file)
        print(image)

       # cv2.imshow('resur',image)


if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())