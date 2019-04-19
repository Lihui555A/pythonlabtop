from PyQt5.Qt import QApplication,QWidget,QTextEdit,QPushButton,QTextImageFormat
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
        tif=QTextImageFormat()
        tif.setName('001_01.png')
        tif.setWidth(50)
        tif.setHeight(50)
        textcursor.insertImage(tif)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())