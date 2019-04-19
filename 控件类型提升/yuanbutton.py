# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yuanbutton.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication,QWidget
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 417)
        self.pushButton = Newpushubtton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 60, 361, 171))
        self.pushButton.setStyleSheet("QPushButton{font: 10pt \"Arial\";}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 85, 0,100);font: 30pt \"Arial\";}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/图片1.jpg"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(27, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))


from newbutton import Newpushubtton
import iamge_rc
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=QWidget()
    mywin=Ui_Form()
    mywin.setupUi(window)
    window.show()
    sys.exit(app.exec_())