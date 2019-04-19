from 复杂界面重复.denglu_pane import denglu
from 复杂界面重复.zhuce_pane import zhuce
from PyQt5.Qt import QApplication,QWidget,QLabel
from PyQt5.QtCore import QPropertyAnimation,QPoint,QAbstractAnimation,QEasingCurve
import sys


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=zhuce()  #小猫
    denglu_pane=denglu(window) #这个只是为了做动画先给这个窗口放个开始的位置，这样就看不到了
    denglu_pane.move(0,window.height())
    denglu_pane.show()
    def exit_denglu_pane_func():
        animation = QPropertyAnimation(denglu_pane)  # 谁要动就给谁做
        animation.setTargetObject(denglu_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(window.width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    denglu_pane.exit_signal.connect(exit_denglu_pane_func)
    def show_denglu_pane_func():
        animation=QPropertyAnimation(denglu_pane) #谁要动就给谁做
        animation.setTargetObject(denglu_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(denglu_pane.pos())
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    window.show_denglu_pane_signal.connect(show_denglu_pane_func)
    def print_zhanghao_mima(zhanhao,mima):
        print(zhanhao,mima)
    denglu_pane.zhuce_signal.connect(print_zhanghao_mima)
    def check_zhanghao_mima(zhanghao,mima):
       if zhanghao=='1'and mima=='1':
           print('账号密码正确')
       else:
           window.show_error_animation()
    window.login_button_clicked_signal.connect(check_zhanghao_mima)
    window.show()
    sys.exit(app.exec_())