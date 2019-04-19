from PyQt5.Qt import QApplication,QWidget,QLineEdit
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        # line_1.textEdited() #文本编辑时发射的信号 ，这个其实和下面的文本内容发生改变时发射的信号是一样的，不一样的地方在这行代码是对用户在界面上对控件进行编辑时才会触发，如果是在代码里改是不会触发的
        # line_1.textChanged()#文本内容发生改变时发生的信号
        # line_1.returnPressed()#按下回车时发生的信号
        # line_1.editingFinished()#编辑完成是发射的信号
        line_1.cursorPositionChanged.connect(self.func)#光标位置发生改变时发射的信号，会传递出光标的老位置和新位置
        # line_1.selectionChanged()#选中的文本发生改变时发射的信号,这里需要注意的是只要选中的内容的光标轻微的移动也会触发信号发射
        self.line=line_1
    def func(self,oldposition,newposition):
        self.line.setSelection(0,newposition)
        print(oldposition,newposition)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())