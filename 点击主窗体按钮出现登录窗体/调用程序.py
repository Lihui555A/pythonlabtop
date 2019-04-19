import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import pyqtSignal
from 点击主窗体按钮出现登录窗体.主窗体 import Ui_MainWindow
from 点击主窗体按钮出现登录窗体.登录窗体 import Ui_Widget
from 点击主窗体按钮出现登录窗体.a import Ui_form1
class Ui_widget(QWidget,Ui_Widget):
    def __init__(self):
        super(Ui_widget, self).__init__()
        self.setupUi(self)
# class Ui_form(QWidget,Ui_Form):
#     def __init__(self):
#         super(Ui_form, self).__init__()
#         self.setupUi(self)
class Ui_mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Ui_mainwindow, self).__init__()
        self.ui_widget=Ui_widget()
        self.ui_form=Ui_form1()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_ui_widget)
        self.ui_widget.denglu.clicked.connect(self.login)
        self.ui_widget.zhuce.clicked.connect(self.open_ui_form)
        self.ui_widget.quxiao.clicked.connect(self.back_mainwindow)
       # self.ui_form.maketure.clicked.connect(self.get_information)
        self.ui_form.cancel.clicked.connect(self.back_ui_widget)
        self.ui_form.sin.connect(lambda str:print(str))
    def open_ui_widget(self):
        self.hide()
        self.ui_widget.show()
    def login(self):
        account= self.ui_widget.lineEdit.text()
        password=self.ui_widget.lineEdit_2.text()
        if account=='123456'and password=='123456':
            print('登录成功')
        else:
            print('登录失败')
    def open_ui_form(self):
        self.hide()
        self.ui_widget.hide()
        self.ui_form.show()
    def back_mainwindow(self):
        self.show()
        self.ui_widget.hide()
    # def get_information(self):
    #     print(self.ui_form.lineEdit.text())
    #     print(self.ui_form.lineEdit_2.text())
    #     print(self.ui_form.lineEdit_3.text())
    #     print(self.ui_form.lineEdit_4.text())
    #     print(self.ui_form.lineEdit_5.text())
    def back_ui_widget(self):
        self.ui_form.hide()
        self.ui_widget.show()



if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=Ui_mainwindow()
    mywin.show()
    sys.exit(app.exec_())