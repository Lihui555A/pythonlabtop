from PyQt5.Qt import QApplication,QWidget,QLabel,QPainterPath
import sys,math
from PyQt5.QtGui import *
from PyQt5.QtCore import QRectF,Qt,QPropertyAnimation,QPointF
class Window(QWidget):
    def __init__(self):
        super().__init__()

class Animation(QPropertyAnimation):

    def __init__(self, target, prop):
        super(Animation, self).__init__(target, prop)

    def updateCurrentTime(self, currentTime):
        self.m_path = QPainterPath()
        if self.m_path.isEmpty():
            end = self.endValue()
            start = self.startValue()
            self.m_path.addEllipse(QRectF(start, end))
        dura = self.duration()
        if dura == 0:
            progress = 1.0
        else:
            progress = (((currentTime - 1) % dura) + 1) / float(dura)
        easedProgress = self.easingCurve().valueForProgress(progress)
        if easedProgress > 1.0:
            easedProgress -= 1.0
        elif easedProgress < 0:
            easedProgress += 1.0

        pt = self.m_path.pointAtPercent(easedProgress)
        self.updateCurrentValue(pt)

    def startAnimation(self, startx, starty, endx, endy, duration):
        self.setStartValue(QPointF(startx, starty))
        self.setEndValue(QPointF(endx, endy))
        self.setDuration(duration)
        self.setLoopCount(-1)
        self.start()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())