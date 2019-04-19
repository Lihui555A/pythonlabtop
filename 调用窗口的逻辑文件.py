# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow
# from 显示气泡提示信息 import Winform
# class MyMainWindow(QMainWindow,Winform):
#     def __init__(self):
#         super(MyMainWindow,self).__init__()
#         self.initUI()  #这个括号里边是没有self的，因为原来Winform类中已经有继承的窗体了
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from 创建菜单栏和工具栏 import Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)#这个括号里填的self是指的新建的类中的QMainWindow,因为原来的Ui_MainWindow中的setupUi()函数中需要加一个主窗体
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,'打开','C:/','All Files(*);;Text Files(*.txt)')
        self.statusbar.showMessage(file)
if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())