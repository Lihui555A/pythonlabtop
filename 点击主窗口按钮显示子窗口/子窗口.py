# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '子窗口.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 469)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(130, 110, 291, 201))
        self.textEdit.setObjectName("textEdit")
        self.openmianwindow = QtWidgets.QPushButton(Form)
        self.openmianwindow.setGeometry(QtCore.QRect(100, 340, 75, 23))
        self.openmianwindow.setObjectName("openmianwindow")
        self.closewindow = QtWidgets.QPushButton(Form)
        self.closewindow.setGeometry(QtCore.QRect(300, 340, 75, 23))
        self.closewindow.setObjectName("closewindow")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是子窗口的内容</p></body></html>"))
        self.openmianwindow.setText(_translate("Form", "返回主窗口"))
        self.closewindow.setText(_translate("Form", "关闭子窗口"))

