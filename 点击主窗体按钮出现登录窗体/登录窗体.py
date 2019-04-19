# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录窗体.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(515, 381)
        self.widget = QtWidgets.QWidget(widget)
        self.widget.resize(311, 111)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(widget)
        self.widget1.setGeometry(QtCore.QRect(90, 230, 311, 71))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.denglu = QtWidgets.QPushButton(self.widget1)
        self.denglu.setObjectName("denglu")
        self.horizontalLayout.addWidget(self.denglu)
        self.zhuce = QtWidgets.QPushButton(self.widget1)
        self.zhuce.setObjectName("zhuce")
        self.horizontalLayout.addWidget(self.zhuce)
        self.quxiao = QtWidgets.QPushButton(self.widget1)
        self.quxiao.setObjectName("quxiao")
        self.horizontalLayout.addWidget(self.quxiao)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "账号"))
        self.label_2.setText(_translate("widget", "密码"))
        self.denglu.setText(_translate("widget", "登录"))
        self.zhuce.setText(_translate("widget", "注册"))
        self.quxiao.setText(_translate("widget", "取消"))

