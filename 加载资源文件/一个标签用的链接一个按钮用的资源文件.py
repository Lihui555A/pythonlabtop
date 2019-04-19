# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '一个标签用的链接，一个按钮用的资源文件.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 966)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 80, 201, 149))
        self.label.setToolTipDuration(-1)
        self.label.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/picture/1.jpg"))
        self.label.setScaledContents(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 90, 121, 121))
        self.pushButton.setStyleSheet("border-image: url(:/picture/1.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 330, 111, 41))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">这是一个标签</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("Form", "这是一个按钮"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><a href=\"www.taobao.com\"><span style=\" text-decoration: underline; color:#0000ff;\">欢迎访问淘宝网</span></a></p></body></html>"))

import resourse_rc
