from PyQt5.Qt import QApplication,QWidget,QLineEdit,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        line_1.move(100,100)
        line_2 = QLineEdit(self)
        line_2.move(100, 200)
        line_3 = QLineEdit(self)
        line_3.move(100, 300)
        self.line1=line_1
        self.line2=line_2
        self.line3=line_3
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(400,400)
        self.button=button
        self.button.clicked.connect(self.func)
    def func(self):
        #self.line1.setSelection(0,2) #选中文本框中的文字，参数第一个是开始的位置，第二个是长度
        # self.line1.selectAll()#选中文本框的所有内容，就是全选
        # self.line1.deselect()#取消选中
        # self.line1.hasSelectedText()#判断是否有选中的文本
        print(self.line1.selectedText())#获取选中的文本
        print(self.line1.selectionStart())#获取选中的文本的开始的位置
        print(self.line1.selectionLength())#获取的选中的文本的长度，在跑这行代码之前要先用代码把文本框里的内容给选中了

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())