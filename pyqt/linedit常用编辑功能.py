from PyQt5.Qt import QApplication,QWidget,QLineEdit,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        line_1.setText('dfdfd')
        line_1.move(100,100)
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(200,200)
        button.clicked.connect(self.func)
        self.line=line_1
        line_2=QLineEdit(self)
        line_2.move(300,300)
        self.line2=line_2
        self.line2.setDragEnabled(True) #设置控件内选中文本支持拖拽动作
    def func(self):
        # self.line.backspace()#相当于键盘上的backspace
        # self.line.clear()#清空内容
        # self.line.copy()#复制内容
        # self.line.cut()
        # self.line.paste()
        # self.line.undo()#撤销
        # self.line.setFocus()#获取焦点
        # self.line.setCursorPosition(0)#设置鼠标的位置
        # self.line.setFocus()
        pass




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())