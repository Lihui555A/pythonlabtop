import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from 点击主窗口按钮显示子窗口.主窗口 import Ui_MainWindow
from 点击主窗口按钮显示子窗口.子窗口 import Ui_Form
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)#这个括号里填的self是指的新建的类中的QMainWindow,因为原来的Ui_MainWindow中的setupUi()函数中需要加一个主窗体
        self.children=MyUi_Form()
        self.children.closewindow.clicked.connect(self.Closechildwindow)
        self.children.openmianwindow.clicked.connect(self.Openmainwindow)
        self.pushButton.clicked.connect(self.openchildwidget)
    def openchildwidget(self): #这个是主窗口调用子窗口的
        self.hide()
        self.children.show()
    def Closechildwindow(self):
        self.children.close()
    def Openmainwindow(self):
        self.children.hide()
        self.show()

class MyUi_Form(QWidget,Ui_Form):
    def __init__(self):#这个括号里的self是代表的是QWidget，就是最底下的那个衬布，其实，这个衬布用QWidget还是用QMainwindow取决于Ui_Form的setup_ui函数里需要的是Qwidget还是Qmainwidow
        super(MyUi_Form,self).__init__()
        self.setupUi(self)
     #   self.mywindow=MyMainWindow()
    #     self.closewindow.clicked(self.Closewindow)
    #     self.openmianwindow.clicked(self.Openmianwindow)

    def Openmianwindow(self):
        pass
    def Closewindow(self):
        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())