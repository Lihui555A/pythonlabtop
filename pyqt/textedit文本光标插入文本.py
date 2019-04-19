from PyQt5.Qt import QApplication,QWidget,QTextEdit,QPushButton,QTextCharFormat
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QTextEdit(self)
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(400,100)
        button.clicked.connect(self.func)
        self.button=button
        self.line=line_1
    def func(self):

        textcursor=self.line.textCursor()#获取文本光标
        tcf=QTextCharFormat() #这句话是用来设计文本格式的
        tcf.setToolTip('这是一个实验')#文本字符的格式
        tcf.setFontFamily('隶书') #文本字符的格式
        tcf.setFontPointSize(30) #文本字符的格式
        textcursor.insertText('哈哈哈哈哈',tcf)#用这种方法插入的时候可以插入文本字符格式,两个参数一个是文本内容，一个是文本格式






if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())