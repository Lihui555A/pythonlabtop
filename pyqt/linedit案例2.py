from PyQt5.Qt import QApplication,QWidget,QLineEdit,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500, 500)
        # 输出模式设置
        line_1 = QLineEdit(self)
        line_1.move(100, 100)

        line_2 = QLineEdit(self)
        line_2.move(100, 200)
        line_2.setEchoMode(2)
        button=QPushButton(self)
        button.setText('登录')
        button.clicked.connect(self.log)
        self.line_1=line_1
        self.line2=line_2
        self.button=button
        self.button.setEnabled(False)
        self.line_1.textChanged.connect(self.button_able)
        self.line2.textChanged.connect(self.button_able)
        self.line_1.setPlaceholderText('请输入账号') #设置站位文本
        self.line2.setPlaceholderText('请输入密码')
        self.line2.setClearButtonEnabled(True)
    def log(self):
        logtext=self.line_1.text()
        password=self.line2.text()
        if logtext!='123':
            self.line_1.setText('')
            self.line2.setText('')

        if password!='456':
            self.line2.setText('')
    def button_able(self):
        if self.line_1.text()!=''and self.line2.text()!='':
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())