from PyQt5.Qt import QApplication,QWidget,QPushButton,QLabel
from PyQt5 import QtCore
from PyQt5.QtCore import QThread,QDateTime,pyqtSignal
import sys,time




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QPushButton(self)
        line_1.setText('我是按钮')
        line_1.setObjectName('btn')
        self.label=QLabel(self)
        self.label.setText('我是标签')
        self.label.move(100,100)


        QtCore.QMetaObject.connectSlotsByName(self)#要用下面的东西就得加这句话
    @QtCore.pyqtSlot()
    def on_btn_clicked(self):
        self.label.setText('hheheh')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())