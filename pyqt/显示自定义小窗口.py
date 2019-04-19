# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '显示自定义小窗口.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.show_window)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
    def show_window(self):
        self.window = QtWidgets.QWidget()
        lable=QtWidgets.QLabel(self.window)
        lable.setScaledContents(True)
        lable.resize(1000,500)
        lable.setPixmap(QPixmap('1.jpg'))

        self.window.show()







if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    win=QtWidgets.QWidget()
    mywin=Ui_Form()
    mywin.setupUi(win)
    win.show()
    sys.exit(app.exec_())

