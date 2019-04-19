import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):   #在本例中是创建一个主窗口类然后继承PYQT中正儿八经的主窗口，然后下面那四句话都是原来pyqt主窗口本来就有的的函数或者方法，我们只是拿来调用一下然后运用在自己创建的这个窗口的类上
    def __init__(self):
        super().__init__()
        self.resize(400,200)    #这个歌方法是改变窗口大小的
        self.status=self.statusBar()    #这个方法是获取父类的状态栏对象，啥意思，self.statusBar()这句话是父类的一个小子类吧，用来返回状态栏的一些信息，self.status是用来实例化这个小子类的，
        self.status.showMessage('这是状态栏提示',5000)#self.status.showMessage然后这个实例化的状态栏对象调用showMessage方法用来在状态栏上显示一些信息
        self.setWindowTitle('主窗口状态栏提示的例子')  #当然主窗口父类中还有一些别的方法，具体可以看书124页


if __name__=='__main__':
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
