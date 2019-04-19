# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("\n"
"QWidget#Form{\n"
"border-image: url(:/register/images/sky.jpg);}")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(90, 20, 50, 50))
        self.about_menue_btn.setStyleSheet("QPushButton{background-color:rgb(255, 0, 255);\n"
"border:2px solid white;\n"
"border-radius:25px;\n"
"color: rgb(193, 255, 237);}\n"
"QPushButton:hover{\n"
"border:4px double black;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(170, 255, 0);\n"
"color:blue;\n"
"}")
        self.about_menue_btn.setCheckable(False)
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(100, 90, 50, 50))
        self.reset_menue_btn.setStyleSheet("QPushButton{background-color:rgb(255, 0, 255);\n"
"border:2px solid white;\n"
"border-radius:25px;\n"
"color: rgb(193, 255, 237);}\n"
"QPushButton:hover{\n"
"border:4px double black;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(170, 255, 0);\n"
"color:blue;\n"
"}")
        self.reset_menue_btn.setCheckable(False)
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(20, 90, 50, 50))
        self.exit_menue_btn.setStyleSheet("QPushButton{background-color:rgb(255, 0, 255);\n"
"border:2px solid white;\n"
"border-radius:25px;\n"
"color: rgb(193, 255, 237);}\n"
"QPushButton:hover{\n"
"border:4px double black;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(170, 255, 0);\n"
"color:blue;\n"
"}")
        self.exit_menue_btn.setCheckable(False)
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.main_menue_btn.setStyleSheet("QPushButton{background-color:rgb(255, 0, 255);\n"
"border:2px solid white;\n"
"border-radius:25px;\n"
"color: rgb(193, 255, 237);}\n"
"QPushButton:hover{\n"
"border:4px double black;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(170, 255, 0);\n"
"color:blue;\n"
"}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(91, 200, 301, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:rgb(243, 243, 243);font: 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_line.setMinimumSize(QtCore.QSize(0, 35))
        self.account_line.setStyleSheet("background-color:transparent;\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(249, 249, 249);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"")
        self.account_line.setClearButtonEnabled(True)
        self.account_line.setObjectName("account_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_line)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:rgb(243, 243, 243);font: 14pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_line.setMinimumSize(QtCore.QSize(0, 35))
        self.password_line.setStyleSheet("background-color:transparent;\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(249, 249, 249);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"")
        self.password_line.setClearButtonEnabled(True)
        self.password_line.setObjectName("password_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_line)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(243, 243, 243);font: 14pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confirm_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_line.setMinimumSize(QtCore.QSize(0, 35))
        self.confirm_line.setStyleSheet("background-color:transparent;\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(249, 249, 249);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"")
        self.confirm_line.setClearButtonEnabled(True)
        self.confirm_line.setObjectName("confirm_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_line)
        self.regis_button = QtWidgets.QPushButton(self.layoutWidget)
        self.regis_button.setEnabled(False)
        self.regis_button.setMinimumSize(QtCore.QSize(0, 45))
        self.regis_button.setStyleSheet("QPushButton{background-color: rgb(0, 85, 0);color:white;\n"
"font: 14pt \"微软雅黑\";border-radius:20px}\n"
"QPushButton:hover{background-color:rgb(170, 255, 127);color:black}\n"
"QPushButton:pressed{background-color: rgb(85, 255, 255);color:yellow}\n"
"QPushButton:disabled{background-color: gray;color:yellow}\n"
"")
        self.regis_button.setObjectName("regis_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.regis_button)

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about_button_click)
        self.exit_menue_btn.clicked.connect(Form.exit_button_click)
        self.reset_menue_btn.clicked.connect(Form.reset_button_click)
        self.regis_button.clicked.connect(Form.register_button_click)
        self.account_line.textChanged['QString'].connect(Form.regis_button_enabled)
        self.password_line.textChanged['QString'].connect(Form.regis_button_enabled)
        self.confirm_line.textChanged['QString'].connect(Form.regis_button_enabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.reset_menue_btn.setText(_translate("Form", "重置"))
        self.exit_menue_btn.setText(_translate("Form", "退出"))
        self.main_menue_btn.setText(_translate("Form", "菜单"))
        self.label.setText(_translate("Form", "账       号："))
        self.label_2.setText(_translate("Form", "密       码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.regis_button.setText(_translate("Form", "注册"))


from PyQt5_Demo import image_rc
