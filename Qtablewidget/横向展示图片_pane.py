from PyQt5.Qt import QApplication,QWidget,QLabel,QIcon,QAbstractItemView,QPushButton,QPixmap
from 横向展示图片 import Ui_Form
import sys
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QFileDialog
from PyQt5.QtCore import QSize,QThread,pyqtSignal
from PyQt5 import QtGui
from PIL import Image

class Window(QWidget,Ui_Form):
    detect_signal=pyqtSignal(list)
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.setupUi(self)
        self.tableWidget.resize(1081, 270)
    def dabou_click_bigger(self,a,b):#这里会传过来双击的位置
       # print(self.tableWidget.item(a+1,b).text()) #打出来的是图片下方的路径
        image = Image.open(self.tableWidget.item(a+1,b).text())
        button=My_button(self)
        button.setObjectName('big_button')
        button.setStyleSheet("My_button#big_button{border-image: url(%s)}"%(self.tableWidget.item(a+1,b).text()))
        button.resize(image.width*1.5, image.height*1.5)
        button.move((self.width()-button.width())/2,(self.height()-button.height())/2)
        button.show()
    def single_click_give_indexx(self):
        pass
    def open_files(self):
        files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择",   "./", "All Files (*.jpg);;Text Files (*.jpg)")
        if ok1:
            self.tableWidget.setColumnCount(len(files))
            self.tableWidget.setRowCount(2)
            self.tableWidget.setIconSize(QSize(300, 200))  # 设置图标的大小
            for index, file_name in enumerate(files):  # i是索引值，index是文件名
                table_widget_item_1 = QTableWidgetItem(file_name)
                icon = QIcon(file_name)
                table_widget_item_2 = QTableWidgetItem()
                table_widget_item_2.setIcon(icon)
                self.tableWidget.setItem(1, index, table_widget_item_1)  # 参数要行，列，tablewidgetitem
                self.tableWidget.setItem(0, index, table_widget_item_2)
                self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
                self.tableWidget.resizeColumnsToContents()  # 自动适应大小
                self.tableWidget.resizeRowsToContents()  # 自动适应大小
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.hideRow(1)  # 隐藏某一行
                # self.tableWidget.setShowGrid(False)#隐藏表格线
    def start_detect(self):
        picture_filepath_to_detect_list=[]
        for i in range(self.tableWidget.columnCount()):
            picture_filepath_to_detect_list.append(self.tableWidget.item(1,i).text())
        self.detector=WorkThread(picture_filepath_to_detect_list) #实例化线程的时候要注意一定得绑到控件身上
        self.detector.start()
    def delete_pictures(self):
        if self.tableWidget.currentColumn()>=0:
            print(self.tableWidget.selectedItems())
            self.tableWidget.removeColumn(self.tableWidget.currentColumn())
        else:
            pass
class My_button(QPushButton):
    def __init__(self,window):
        super(My_button, self).__init__(window)
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):
        self.close()
class WorkThread(QThread):
    def __init__(self,list):
        super(WorkThread, self).__init__()#这个必须得记住了，线程在实例化传参的时候不需要往这个括号里传参
        self.list=list
    def run(self):
        for i in self.list:
            print(i)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())