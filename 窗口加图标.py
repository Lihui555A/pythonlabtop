import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon
class Icon(QWidget):
    def __init__(self):
        super(Icon,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('程序图标')
        self.setWindowIcon(QIcon(r'.\Icon\beautiful\shadow\grey\ico\001_01.ico'))
if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=Icon()
    icon.show()
    sys.exit(app.exec_())