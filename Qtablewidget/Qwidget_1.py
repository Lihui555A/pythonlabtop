from PyQt5.Qt import QApplication,QWidget,QLabel,QTableWidget,QTableWidgetItem,QIcon,QPixmap,QPushButton
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtCore import pyqtSignal,QThread,QSize,Qt
Qt.RightButton
import os
import requests

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1321, 758)
        self.tableWidget = Mytable_widget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(120, 180, 801, 341))
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(1)
        self.tableWidget.mou
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class Mytable_widget(QTableWidget):
    picture_pah_signal=pyqtSignal(str)
    def __init__(self,window):
        super(Mytable_widget, self).__init__(window)
        self.setAcceptDrops(True)
        self.list=[]
      #  self.setIconSize(QSize(300, 200))
    # def make_icon(self,path):
    #     self.load_icon=QIcon(path)
    #     self.item_2 = QTableWidgetItem()
    #     self.item_2.setIcon(self.load_icon)
    #     # self.insertColumn(0)
    #     # self.insertRow(0)
    #     self.setItem(0, 0, self.item_2)
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent):
        if e.mimeData().text():
            path=e.mimeData().text()[8:]
            if path not in self.list:
                self.list.append(path)
                self.button = QPushButton(self)
                self.button.setObjectName('big_button')
                self.button.setAcceptDrops(True)
                self.button.setStyleSheet(
                    "QPushButton#big_button{border-image: url(%s)}" % (path))
                self.button.resize(300, 200)
                self.insertColumn(0)
                self.setRowHeight(0, 200)
                self.setColumnWidth(0, 300)
                self.setCellWidget(0, 0, self.button)
            else:
                pass




    #         self.load_icon = QIcon(path)
    #         self.item_2 = QTableWidgetItem()
    #         self.item_2.setIcon(self.load_icon)
    #         self.insertColumn(0)
    #         # for i in range(self.columnCount()):
    #         #     self.setColumnWidth(i,300)
    #         # for i in range(self.rowCount()):
    #         #     self.setRowHeight(i,200)
    #         self.setColumnWidth(0, 300)
    #         self.setRowHeight(0, 200)
    #         self.setItem(0, 0, self.item_2)

            # newpath=e.mimeData().text()[-8:-4].replace('%','9')
            # self.load_picture=load_picture_thread(e.mimeData().text(),'%s.jpg'%(newpath))
            # self.load_picture.loaded_picture_path.connect(self.make_icon)
            # self.load_picture.start()

    # def dropEvent(self, e):
    #     if e.mimeData().text():
    #         path=e.mimeData().text()[8:]
    #         print(path)
    #         self.button=QPushButton(self)
    #         self.button.setAcceptDrops(True)
    #         self.button.setObjectName('big_button')
    #         self.button.setStyleSheet(
    #             "QPushButton#big_button{border-image: url(%s)}" % (path))
    #         self.button.resize(300,200)
    #         self.insertColumn(0)
    #         self.setCellWidget(0,0,self.button)
    #         self.setRowHeight(0,200)
    #         self.setColumnWidth(0,300)

class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__() #这句话的意思是要把父类的构造函数给调用过来，使得自己的构造函数中包含父类的构造函数
        self.setWindowTitle('第二个窗体') #self代表的对象本身
        self.setupUi(self)
        self.resize(300,300)
        self.tableWidget.move(0,0)
       # self.tableWidget.resizeColumnsToContents()  # 自动适应大小
        #self.tableWidget.resizeRowsToContents()
        # self.tableWidget.verticalHeader().setVisible(False)
        #self.tableWidget.hideRow(1)
# class load_picture_thread(QThread):
#     loaded_picture_path=pyqtSignal(str)
#     def __init__(self,url,path):
#         super(load_picture_thread, self).__init__()
#         self.url=url
#         self.path=path
#     def run(self):
#         print(self.url)
#         req = requests.get(self.url)
#         with open(self.path, "wb") as f:  # 开始写文件，wb代表写二进制文件
#             f.write(req.content)
#         self.loaded_picture_path.emit(os.path.join(os.path.abspath('.'),self.path))
#需要两个事件
#dragEnterEvent    #进入控件时触发
#dropEvent         #放下时触
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())