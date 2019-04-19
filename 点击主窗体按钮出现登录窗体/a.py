from 点击主窗体按钮出现登录窗体.注册窗体 import Ui_Form
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import pyqtSignal
class Ui_form1(QWidget,Ui_Form):
    sin=pyqtSignal(str)
    def __init__(self):
        super(Ui_form1, self).__init__()
        self.setupUi(self)
    def get_world(self):

        self.sin.emit('woaini')
        self.label.setText('hehehe')
if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=Ui_form1()
    mywin.show()
    sys.exit(app.exec_())