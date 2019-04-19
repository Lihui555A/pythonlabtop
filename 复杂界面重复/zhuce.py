# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 413)
        Form.setMinimumSize(QtCore.QSize(459, 413))
        Form.setMaximumSize(QtCore.QSize(459, 413))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.donghua_lable = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donghua_lable.sizePolicy().hasHeightForWidth())
        self.donghua_lable.setSizePolicy(sizePolicy)
        self.donghua_lable.setStyleSheet("")
        self.donghua_lable.setText("")
        self.donghua_lable.setObjectName("donghua_lable")
        self.verticalLayout_2.addWidget(self.donghua_lable)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox.setStyleSheet("QComboBox {font-size:20pt;border:none;border-bottom:1px solid lightgray;background-color:transparent;}\n"
"QComboBox:hover{border-bottom:gray}\n"
"QComboBox:focus{border-bottom:1px solid rgb(18,183,245);}\n"
"QComboBox::drop-down{background-dolor:transparent;width:60px;height:40px;}\n"
"QComboBox::down-arrow{image:url(:/image/accept.png);width:40px;height:20px;}\n"
"QComboBox QAbstractItemView{min-height40px;}\n"
"QComboBox QAbstractItemView:item{color:lightblue;}\n"
"\n"
"\n"
"")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/application_form.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/application_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 38))
        self.lineEdit.setStyleSheet("QLineEdit{font-size:20pt;border:none;border-bottom:1px solid lightgray;background-color:transparent;}\n"
"QLineEdit:hover{border-bottom:1px solid gray;}\n"
"QLineEdit:focus{border-bottom:1px solid rgb(18,183,145);}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setStyleSheet("QPushButton{background-color:blue;border-radius:10px;color:white;spacing:30px;}\n"
"QPushButton:hover{background-color:lightblue;}\n"
"QPushButton:pressed{background-color:black;}\n"
"\n"
"QPushButton:disabled{background-color:gray;}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/application_get.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setStyleSheet("border-image: url(:/image/1.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 4)
        self.horizontalLayout_3.addWidget(self.widget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.show_denglu_pane)
        self.comboBox.editTextChanged['QString'].connect(Form.denglu_button_ennable)
        self.lineEdit.textChanged['QString'].connect(Form.denglu_button_ennable)
        self.checkBox.clicked['bool'].connect(Form.zidongdenglu_button_clicked)
        self.checkBox_2.clicked['bool'].connect(Form.jizhumima_button_clicked)
        self.pushButton_3.clicked.connect(Form.login_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.comboBox.setItemText(0, _translate("Form", "12345"))
        self.comboBox.setItemText(1, _translate("Form", "23456"))
        self.checkBox.setText(_translate("Form", "自动登录"))
        self.checkBox_2.setText(_translate("Form", "记住密码"))
        self.pushButton_3.setText(_translate("Form", "安全登录"))


import denglu_rc
