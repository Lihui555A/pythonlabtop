import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Combo(QComboBox):
    def __init__(self):
        super(Combo,self).__init__()
        self.setAcceptDrops(True) #接受动作开启
    def dragEnterEvent(self,e):#这个是接受者的事件，一旦施加者进入接受者的领地，接受者要发生的事件
        print(e)
        if e.mimeData().hasText():#minedata是一种笼统的数据类型，其中可能包含有文本，视频，图片，网页，音乐等等
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())#施加者把东西放下之后，接受者要发生的事件
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(300,300)
        lo=QFormLayout()
        lo.addRow(QLabel('请把左边的文本拖拽到右边的下拉菜单中'))
        edit=QLineEdit()
        edit.setDragEnabled(True)#施加者开启能够拖动功能
        com=Combo()
        lo.addRow(edit,com)
        self.setLayout(lo)
        self.setWindowTitle('简单的拖拽例子')
if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec_())