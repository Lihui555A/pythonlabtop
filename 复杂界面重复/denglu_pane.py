from PyQt5.Qt import QApplication,QWidget,QLabel,QMessageBox
from PyQt5.QtCore import Qt,QSequentialAnimationGroup,QPropertyAnimation,QAbstractAnimation,QEasingCurve,pyqtSignal
import sys
from 复杂界面重复.denglu import Ui_Form
class denglu(QWidget,Ui_Form):
    exit_signal=pyqtSignal()
    zhuce_signal = pyqtSignal(str,str)
    def __init__(self,parent=None,*args,**kwargs): #这里后边直接写一个形参就行了，不用写那么多
        super().__init__(parent,*args,**kwargs) #这里也一样直接写一个简单点的参数就可以了
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.animation_targets = [self.guanyu_button, self.tuichu_button, self.chongzhi_button]#参加动画的控件
        self.animation_targets_pos = [target.pos() for target in self.animation_targets] #参加动画控件的开始位置
        self.hehe_button_pos=self.hehe_button.pos()
        self.denglu_button.setEnabled(False)
        self.hehe_button_position=self.hehe_button.pos()
    def caidan_button_clicked(self,checked):

        if checked: #如果是被选中就
            animation_group = QSequentialAnimationGroup(self)  # 创建一个动画组
            for index, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()  # 创建一个属性动画实例
                animation.setTargetObject(target)  # 添加目标控件
                animation.setPropertyName(b'pos')  # 设置要参与动画的属性
                animation.setStartValue(self.animation_targets_pos[index])
                animation.setEndValue(self.caidan_button.pos())
                animation.setDuration(500)
                animation.setEasingCurve(QEasingCurve.InOutBounce)
                animation_group.addAnimation(animation)
            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        else:
            animation_group = QSequentialAnimationGroup(self)  # 创建一个动画组
            for index, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()  # 创建一个属性动画实例
                animation.setTargetObject(target)  # 添加目标控件
                animation.setPropertyName(b'pos')  # 设置要参与动画的属性
                animation.setStartValue(self.caidan_button.pos())
                animation.setEndValue(self.animation_targets_pos[index])
                animation.setDuration(500)
                animation.setEasingCurve(QEasingCurve.InOutBounce)
                animation_group.addAnimation(animation)
            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
    def guanyu_button_clicked(self):
        QMessageBox.about(self,'关于','这是一个关于对话框')
    def tuichu_button_clicked(self):
        self.exit_signal.emit()
    def chongzhi_button_clicked(self):
        self.zhanghao_linedit.clear()
        self.mima_linedit.clear()
        self.querenmima_linedit.clear()
    def zhuce_button_clicked(self):
        zhanghao=self.zhanghao_linedit.text()
        mima=self.mima_linedit.text()
        self.zhuce_signal.emit(zhanghao,mima)
    def haha_button_clicked(self,checked):
        if checked:
            animation = QPropertyAnimation(self)
            animation.setTargetObject(self.hehe_button)  # 添加目标控件
            animation.setPropertyName(b'pos')  # 设置要参与动画的属性
            animation.setStartValue(self.hehe_button.pos())
            animation.setEndValue(self.haha_button.pos())
            animation.setDuration(500)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation.start(QAbstractAnimation.DeleteWhenStopped)
        else:
            animation= QPropertyAnimation(self)
            animation.setTargetObject(self.hehe_button)  # 添加目标控件
            animation.setPropertyName(b'pos')  # 设置要参与动画的属性
            animation.setEndValue(self.hehe_button_position)
            animation.setStartValue(self.haha_button.pos())
            animation.setDuration(500)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation.start(QAbstractAnimation.DeleteWhenStopped)
    def hehe_button_clicked(self):
        pass
    def denglu_button_enable(self):
        if len(self.zhanghao_linedit.text())>0 and len(self.mima_linedit.text())>0 and len(self.querenmima_linedit.text())>0 and self.mima_linedit.text()==self.querenmima_linedit.text():
            self.denglu_button.setEnabled(True)
        else:
            self.denglu_button.setEnabled(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=denglu()
    window.zhuce_signal.connect(lambda a,b:print(a,b))

    window.show()
    sys.exit(app.exec_())