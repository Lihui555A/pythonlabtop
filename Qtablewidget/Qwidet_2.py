# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '支持拖放图片.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Qtablewidget.Qwidget_1 import Mytable_widget
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1321, 758)
        self.tableWidget = Mytable_widget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(120, 180, 801, 341))
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

