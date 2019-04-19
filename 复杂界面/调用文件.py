from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
from 复杂界面.register_jiemian import  Register_jiemian
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.register_panel=Register_jiemian()
        self.register_panel.exit_signal.connect(self.func_2)
        self.register_panel.register_account_pwd_signal.connect(self.func_3)
        self.button=QPushButton(self)
        self.button.clicked.connect(self.func)
        self.resize(500,500)
        self.button.setText('显示注册界面')
    def func(self):
        self.hide()
        self.register_panel.show()
    def func_2(self):
        self.register_panel.hide()
        self.show()
    def func_3(self,a,b):
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())