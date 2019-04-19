from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtCore import QAnimationGroup,QPropertyAnimation,QPoint,QRect,QEasingCurve,QAbstractAnimation,QParallelAnimationGroup,QSequentialAnimationGroup

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

    def moved(self):        #并行动画组，同时执行
        # animation_group=QParallelAnimationGroup() #创建动画组
        animation_group=QSequentialAnimationGroup() #创建一个顺序动画执行组，这个动画组在加两个动画的中间可以加一个addpause(5000)括号里的参数表示两个动画之间间隔的时间
        # animation_group.addAnimation()#添加动画
        # animation_group.removeAnimation()#移除动画
        # animation_group.animationAt(index)#获取动画
        # animation_group.takeAnimation(index)#获取并移除动画
        # animation_group.animationCount()#获取动画的个数
        # animation_group.clear()#清除动画
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self.button)
        animation.setPropertyName(b'geometry')
        animation.setStartValue(QRect(0,0,0,0))  #用这两句话的时候就得用geometry了
        animation.setKeyValueAt(0.5,QRect(400,0,200,200)) #这里可以实现中间状态
        animation.setKeyValueAt(0.7,QRect(0,400,50,50))
        animation.setEndValue(QRect(400,400,100,100))                  #常用的还有size还有windowOpacity
        animation.setLoopCount(100)
        animation.setEasingCurve(QEasingCurve.InOutBounce)
        print(animation.loopCount())#打印出的是动画执行的总的遍数
        print(animation.currentLoop())#打印出当前动画执行的第几遍
        print(animation.duration())#打印出动画执行单次的时长
        print(animation.totalDuration())#打印出动画执行完需要的总的时长
        animation.setDuration(3000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)#动画停止时自动删除，括号里也可以不写这么长的参数
#

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())