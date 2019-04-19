# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
startnum=0
endnum=0

class Thread(QThread):
    sinout=pyqtSignal(str)#自定义一个能够传参的信号
    def __init__(self):
        super(Thread,self).__init__()
    def run(self):
        for i in range(100000000):
            if i%100000==0:
                self.sinout.emit(str(i))

class Thread_2(QThread):
    sinout=pyqtSignal(str)#自定义一个能够传参的信号
    def __init__(self):
        super(Thread_2,self).__init__()
    def run(self):
        for i in range(10000000000000):
            if i%100000==0:
                self.sinout.emit(str(i))


class Thread_1(QThread):
    def __init__(self):
        super(Thread_1,self).__init__()
    def run(self):
        #ui=Ui_MainWindow()
        for i in range(100000000,100000000000000):
            #ui.label.setText(str(i))
            print(i)





class Ui_MainWindow(object):#自动生成的主窗体，代码是自动创建的是父类
    def setupUi(self, MainWindow): #因为没有继承关系所以直接用的是函数，函数中有一个参数是需要传一个主窗体的，这个主窗体是个实例化的主窗体对象，需要在下面实例化出来，然后放到调用的这个函数中
        MainWindow.setObjectName("MainWindow")#这个实例化的窗体具有的方法，给自己定名字
        MainWindow.resize(800, 600)#窗体自有的方法给自己定大小
        self.centralwidget = QtWidgets.QWidget(MainWindow)#这里的self.centralwidget可以看成是这个类的一些属性中心控件要放在主窗口上
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #按钮放在中心控件上
        self.pushButton.setGeometry(QtCore.QRect(140, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 290, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 140, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget) #主窗口中心控件落实
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.start)  #按钮链接槽函数
        self.pushButton_2.clicked.connect(self.end)  #按钮链接槽函数
        self.thread=Thread()   #  实例化一个线程
        self.thread_1 = Thread_1()  #实例化一个线程
        self.thread_2 = Thread_2()  #实例化一个线程
        self.thread.sinout.connect(self.p1)
        self.thread_2.sinout.connect(self.p2)

    def p1(self,str):
        self.label.setText(str)
    def p2(self,str):
        self.label_2.setText(str)
    def start(self):
        self.thread.start()
       # self.thread_2.start()
       # self.thread_1.start()
    def end(self):
        self.thread_1.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "打字"))
        self.pushButton_2.setText(_translate("MainWindow", "显示数字"))
        self.label.setText(_translate("MainWindow", "显示文字"))
        self.label_2.setText(_translate("MainWindow", "显示数字"))

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    UI=Ui_MainWindow()
    UI.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
