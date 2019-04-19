from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import sys
class Winform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口居中显示')
        self.resize(370,250)
        self.center()
    def center(self):
        screen= QDesktopWidget().screenGeometry()#QDesktopWidget描述显示屏幕的类，调用screenGeometry()方法获得屏幕大小
        size=self.geometry()#自己创建的窗体的大小和位置
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

if __name__=="__main__":
    app=QApplication(sys.argv)
    winform=Winform()
    winform.show()
    sys.exit(app.exec_())
