


from PyQt5.Qt import *
from pyqt与OpenCV结合 import Ui_Form
import sys
from PyQt5.QtCore import Qt

class myLabel(QLabel):
    def __init__(self,window):
        super(myLabel, self).__init__(window)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.setPixmap(QPixmap('1.jpg'))


    def mousePressEvent(self, event):

        self.x0 = event.x()
        self.y0 = event.y()

    def mouseMoveEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawRect(rect)
        # pqscreen = QGuiApplication.primaryScreen()
        # pixmap2 = pqscreen.grabWindow(self.winId(), self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        # pixmap2.save('555.png')

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.label=myLabel(self)
        self.label.resize(300,300)
        self.startTimer(10)

    def timerEvent(self, event):
        self.label_2.setPixmap(QPixmap('555.png'))
        self.label_2.resize(300,300)









if __name__ == '__main__':
    app=QApplication(sys.argv )
    mywin=Mywin()
    mywin.show()
    sys.exit(app.exec_())
