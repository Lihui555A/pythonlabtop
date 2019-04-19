from PyQt5.Qt import QWidget,QApplication,QComboBox,QListView
from untitled3 import Ui_Form
import sys
class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.listView=Combo()

class Combo(QListView):
    def __init__(self):
        super(Combo,self).__init__()
        self.setAcceptDrops(True) #接受动作开启
    def dragEnterEvent(self,e):#这个是接受者的事件，一旦施加者进入接受者的领地，接受者要发生的事件
        print(e)
        if e.mimeData().hasImage():#minedata是一种笼统的数据类型，其中可能包含有文本，视频，图片，网页，音乐等等
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().imageData())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mywindow=Mywindow()
    mywindow.show()
    sys.exit(app.exec_())
