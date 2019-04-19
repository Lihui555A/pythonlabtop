import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from 窗口居中显示 import Ui_MainWindow
class Mymainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mymainwindow,self).__init__()
        self.setupUi(self)
        self.setFixedSize(500, 500)#这句话用来固定窗口的大小
        self.center()

    def center(self): #将屏幕居中显示的函数
        screen=QDesktopWidget().screenGeometry() #整个屏幕的大小
        size=self.geometry() #自身窗体的大小
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=Mymainwindow()
    mywin.show()
    sys.exit(app.exec_())