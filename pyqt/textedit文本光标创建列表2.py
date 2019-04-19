from PyQt5.Qt import QApplication,QWidget,QTextEdit,QPushButton,QTextListFormat
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
        textcursor=self.line.textCursor()
        tif = QTextListFormat()
        tif.setIndent(3)#设置序号缩进，表示3个table键的距离
        tif.setNumberPrefix('<') #设置列表序号前缀
        tif.setNumberSuffix('>')#设置列表序号后缀
        tif.setStyle(QTextListFormat.ListDecimal)#设置列表序号样式

        textcursor.createList(tif)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())