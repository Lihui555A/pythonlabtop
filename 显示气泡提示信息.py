import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont
class Winform(QWidget):
    def __init__(self):
        super(Winform,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('气泡提示demo')
        QToolTip.setFont(QFont('Cursive',20))
        self.setToolTip('这是一个气泡提示')
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(0,350)
        button.setToolTip('这是一个按钮')
if __name__=="__main__":
    app=QApplication(sys.argv)
    winform=Winform()
    winform.show()
    sys.exit(app.exec_())