from 查看谁发射的信号.查看是谁发射的信号 import Ui_Form
from PyQt5.Qt import *
import sys
import random
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
    def compare_with_computer(self):
        list=['石头','剪刀','布']
        com_str=random.sample(list,1)[0]
        user_str=self.sender().text()  #这里是关键
        if com_str=='石头' and user_str=='剪刀':
            QMessageBox.about(self,'提示','你输了，电脑出的是%s'%(com_str))
        elif com_str=='石头'and user_str=='布':
            QMessageBox.about(self,'提示', '你赢了，电脑出的是%s' % (com_str))
        elif com_str=='石头'and user_str=='石头':
            QMessageBox.about(self,'提示', '你俩打成了平手，电脑出的是%s' % (com_str))
        elif com_str == '剪刀' and user_str == '剪刀':
            QMessageBox.about(self,'提示', '你俩打成了平手，电脑出的是%s' % (com_str))
        elif com_str == '剪刀' and user_str == '布':
            QMessageBox.about(self,'提示', '你输了，电脑出的是%s' % (com_str))
        elif com_str == '剪刀' and user_str == '石头':
            QMessageBox.about(self,'提示', '你赢了，电脑出的是%s' % (com_str))
        elif com_str == '布' and user_str == '剪刀':
            QMessageBox.about(self,'提示', '你赢了，电脑出的是%s' % (com_str))
        elif com_str == '布' and user_str == '布':
            QMessageBox.about(self,'提示', '你俩打成了平手，电脑出的是%s' % (com_str))
        elif com_str == '布' and user_str == '石头':
            QMessageBox.about(self,'提示', '你输了，电脑出的是%s' % (com_str))
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())