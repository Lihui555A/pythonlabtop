from PyQt5.Qt import QApplication,QWidget,QPushButton
import sys
from PyQt5 import QtCore,QtGui
class Newpushubtton(QPushButton):
    def __init__(self,window):
        super(Newpushubtton, self).__init__(window)
    def enterEvent(self, *args, **kwargs):
        self.setIconSize(QtCore.QSize(50, 50))
    def leaveEvent(self, *args, **kwargs):
        self.setIconSize(QtCore.QSize(27, 27))


