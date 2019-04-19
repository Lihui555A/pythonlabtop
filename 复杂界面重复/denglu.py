# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 413)
        Form.setStyleSheet("QWidget#Form{border-image: url(:/image/sky.jpg);}")
        self.caidan_button = QtWidgets.QPushButton(Form)
        self.caidan_button.setGeometry(QtCore.QRect(30, 10, 50, 50))
        self.caidan_button.setMinimumSize(QtCore.QSize(50, 50))
        self.caidan_button.setMaximumSize(QtCore.QSize(50, 50))
        self.caidan_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.caidan_button.setCheckable(True)
        self.caidan_button.setObjectName("caidan_button")
        self.guanyu_button = QtWidgets.QPushButton(Form)
        self.guanyu_button.setGeometry(QtCore.QRect(110, 10, 50, 50))
        self.guanyu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.guanyu_button.setMaximumSize(QtCore.QSize(50, 50))
        self.guanyu_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.guanyu_button.setObjectName("guanyu_button")
        self.tuichu_button = QtWidgets.QPushButton(Form)
        self.tuichu_button.setGeometry(QtCore.QRect(30, 80, 50, 50))
        self.tuichu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.tuichu_button.setMaximumSize(QtCore.QSize(50, 50))
        self.tuichu_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.tuichu_button.setObjectName("tuichu_button")
        self.chongzhi_button = QtWidgets.QPushButton(Form)
        self.chongzhi_button.setGeometry(QtCore.QRect(110, 80, 50, 50))
        self.chongzhi_button.setMinimumSize(QtCore.QSize(50, 50))
        self.chongzhi_button.setMaximumSize(QtCore.QSize(50, 50))
        self.chongzhi_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.chongzhi_button.setObjectName("chongzhi_button")
        self.haha_button = QtWidgets.QPushButton(Form)
        self.haha_button.setGeometry(QtCore.QRect(260, 20, 50, 50))
        self.haha_button.setMinimumSize(QtCore.QSize(50, 50))
        self.haha_button.setMaximumSize(QtCore.QSize(50, 50))
        self.haha_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.haha_button.setCheckable(True)
        self.haha_button.setObjectName("haha_button")
        self.hehe_button = QtWidgets.QPushButton(Form)
        self.hehe_button.setGeometry(QtCore.QRect(350, 20, 50, 50))
        self.hehe_button.setMinimumSize(QtCore.QSize(50, 50))
        self.hehe_button.setMaximumSize(QtCore.QSize(50, 50))
        self.hehe_button.setStyleSheet("QPushButton{background-color:green;color:white;border-radius:25px;}\n"
"QPushButton:hover{background-color:yellow;}\n"
"QPushButton:checked{background-color:red;}")
        self.hehe_button.setObjectName("hehe_button")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 170, 311, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:black;font:15pt;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.zhanghao_linedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.zhanghao_linedit.setMinimumSize(QtCore.QSize(0, 30))
        self.zhanghao_linedit.setStyleSheet("QLineEdit{background-color:transparent;color:25pt;border:none;border-bottom:1px solid black;font: 16pt \"微软雅黑\";color:white}\n"
"")
        self.zhanghao_linedit.setClearButtonEnabled(True)
        self.zhanghao_linedit.setObjectName("zhanghao_linedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zhanghao_linedit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:black;font:15pt;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mima_linedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.mima_linedit.setMinimumSize(QtCore.QSize(0, 30))
        self.mima_linedit.setStyleSheet("QLineEdit{background-color:transparent;color:25pt;border:none;border-bottom:1px solid black;font: 16pt \"微软雅黑\";color:white}\n"
"")
        self.mima_linedit.setClearButtonEnabled(True)
        self.mima_linedit.setObjectName("mima_linedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mima_linedit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:black;font:15pt;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.querenmima_linedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.querenmima_linedit.setMinimumSize(QtCore.QSize(0, 30))
        self.querenmima_linedit.setStyleSheet("QLineEdit{background-color:transparent;color:25pt;border:none;border-bottom:1px solid black;font: 16pt \"微软雅黑\";color:white}\n"
"")
        self.querenmima_linedit.setClearButtonEnabled(True)
        self.querenmima_linedit.setObjectName("querenmima_linedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.querenmima_linedit)
        self.denglu_button = QtWidgets.QPushButton(self.layoutWidget)
        self.denglu_button.setEnabled(False)
        self.denglu_button.setMinimumSize(QtCore.QSize(0, 40))
        self.denglu_button.setStyleSheet("QPushButton{background-color:red;color:black;border-radius:20px;font: 14pt \"微软雅黑\";}\n"
"\n"
":hover{background-color:black;color:red}\n"
":disabled {background-color:rgb(107, 107, 107)}\n"
"")
        self.denglu_button.setObjectName("denglu_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.denglu_button)
        self.guanyu_button.raise_()
        self.tuichu_button.raise_()
        self.chongzhi_button.raise_()
        self.hehe_button.raise_()
        self.layoutWidget.raise_()
        self.caidan_button.raise_()
        self.haha_button.raise_()

        self.retranslateUi(Form)
        self.caidan_button.clicked.connect(Form.caidan_button_clicked)
        self.guanyu_button.clicked.connect(Form.guanyu_button_clicked)
        self.tuichu_button.clicked.connect(Form.tuichu_button_clicked)
        self.chongzhi_button.clicked.connect(Form.chongzhi_button_clicked)
        self.denglu_button.clicked.connect(Form.zhuce_button_clicked)
        self.haha_button.clicked.connect(Form.haha_button_clicked)
        self.hehe_button.clicked.connect(Form.hehe_button_clicked)
        self.zhanghao_linedit.textChanged['QString'].connect(Form.denglu_button_enable)
        self.mima_linedit.textChanged['QString'].connect(Form.denglu_button_enable)
        self.querenmima_linedit.textChanged['QString'].connect(Form.denglu_button_enable)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.caidan_button.setText(_translate("Form", "菜单"))
        self.guanyu_button.setText(_translate("Form", "关于"))
        self.tuichu_button.setText(_translate("Form", "退出"))
        self.chongzhi_button.setText(_translate("Form", "重置"))
        self.haha_button.setText(_translate("Form", "哈哈"))
        self.hehe_button.setText(_translate("Form", "呵呵"))
        self.label.setText(_translate("Form", "账    号"))
        self.label_2.setText(_translate("Form", "密    码"))
        self.label_3.setText(_translate("Form", "确认密码"))
        self.denglu_button.setText(_translate("Form", "注册"))


import denglu_rc
