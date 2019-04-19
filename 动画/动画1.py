from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtCore import QAnimationGroup,QPropertyAnimation,QPoint,QRect,QEasingCurve,QAbstractAnimation

import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        self.button=QPushButton(self)
        self.button.resize(100,100)
        self.button.clicked.connect(self.moved)

    def moved(self):
        #animation=QPropertyAnimation(self.button,b'pos',self)#这是一种构造函数
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self.button)
        animation.setPropertyName(b'geometry')

        animation.setStartValue(QRect(0,0,0,0))  #用这两句话的时候就得用geometry了
        animation.setKeyValueAt(0.5,QRect(400,0,200,200)) #这里可以实现中间状态
        animation.setKeyValueAt(0.7,QRect(0,400,50,50))
        animation.setEndValue(QRect(400,400,100,100))                  #常用的还有size还有windowOpacity
        animation.setLoopCount(100)
        # animation.setStartValue(QPoint(0,0))
        # animation.setEndValue(QPoint(400,400))
        animation.setEasingCurve(QEasingCurve.InOutBounce)
        print(animation.loopCount())#打印出的是动画执行的总的遍数
        print(animation.currentLoop())#打印出当前动画执行的第几遍
        print(animation.duration())#打印出动画执行单次的时长
        print(animation.totalDuration())#打印出动画执行完需要的总的时长
        animation.setDuration(3000)
        #animation.setDirection(QAbstractAnimation.Backward)#反着做动画
        # animation.pause()#暂停动画
        # animation.resume()#继续动画
        # animation.stop()#停止动画
        animation.start(QAbstractAnimation.DeleteWhenStopped)#动画停止时自动删除，括号里也可以不写这么长的参数
#点击按钮开始动画，再点击按钮停止动画
    # def stop_start(self):
    #     if animation.state()==QAbstractAnimation.Running:
    #         animation.pause()
    #     elif:
    #         animation.state()==QAbstractAnimation.Paused:
    #         animation.start()
#动画的一些常用的信号
# currentloopchanged 会发射当前运行到哪一遍了
# directionchanged 会发射新的方向
# finished 动画完成会发射这个信号
# statechange  会发射两个第一个是新的状态，第二个是旧的状态
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())