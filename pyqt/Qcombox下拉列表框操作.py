import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QIcon

class ComboxDemo(QWidget):
    def __init__(self,parent=None):
        super(ComboxDemo, self).__init__(parent)
        #设置标题
        self.setWindowTitle('ComBox例子')
        #设置初始界面大小
        self.resize(300,90)

        #垂直布局
        layout=QVBoxLayout()
        #创建标签，默认空白
        self.btn1=QLabel('')

        #实例化QComBox对象
        self.cb=QComboBox()
        #单个添加条目
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        #多个添加条目
        self.cb.addItems(['Java','C#','PHP'])
        self.cb.addItem(QIcon(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\noshadow\standart\ico\001_05.ico'),'html')
        #当下拉索引发生改变时发射信号触发绑定的事件
        self.cb.insertItems(1,['css','qss']) #插入数据，第一个参数是索引
        self.cb.currentIndexChanged.connect(self.selectionchange)

        #控件添加到布局中，设置布局
        layout.addWidget(self.cb)
        layout.addWidget(self.btn1)
        self.setLayout(layout)

    def selectionchange(self,i):
        #标签用来显示选中的文本
        #currentText()：返回选中选项的文本
        self.btn1.setText(self.cb.currentText())
        print('Items in the list are:')
        #输出选项集合中每个选项的索引与对应的内容
        #count()：返回选项集合中的数目
        for count in range(self.cb.count()):
            print('Item'+str(count)+'='+self.cb.itemText(count))
            print('current index',i,'selection changed',self.cb.currentText())

if __name__ == '__main__':
    app=QApplication(sys.argv)
    comboxDemo=ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())
