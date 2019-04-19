from PyQt5.Qt import *
from PyQt5.QtCore import Qt,QSequentialAnimationGroup,QPropertyAnimation,QAbstractAnimation,QEasingCurve,pyqtSignal
from PyQt5_Demo.register import Ui_Form
import sys
class Register_jiemian(QWidget,Ui_Form):
    exit_signal=pyqtSignal()
    register_account_pwd_signal=pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.animation_targets=[self.about_menue_btn,self.exit_menue_btn,self.reset_menue_btn]
        self.animation_targets_pos=[target.pos()for target in self.animation_targets]
    def show_hide_menue(self,checked):
        if not checked:
            animation_group = QSequentialAnimationGroup(self)  # 创建一个动画组
            for index,target in enumerate(self.animation_targets):
                animation=QPropertyAnimation()#创建一个属性动画实例
                animation.setTargetObject(target)#添加目标控件
                animation.setPropertyName(b'pos') #设置要参与动画的属性
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.animation_targets_pos[index])
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
                animation.setStartValue(self.animation_targets_pos[index])
                animation.setEndValue(self.main_menue_btn.pos())
                animation.setDuration(500)
                animation.setEasingCurve(QEasingCurve.InOutBounce)
                animation_group.addAnimation(animation)
            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
    def about_button_click(self):
        QMessageBox.about(self,'关于提示','这是一个关于窗口')
    def exit_button_click(self):
        self.exit_signal.emit()
    def reset_button_click(self):
        self.account_line.clear()
        self.password_line.clear()
        self.confirm_line.clear()
    def register_button_click(self):
        account_txt = self.account_line.text()
        password_txt = self.password_line.text()
        self.register_account_pwd_signal.emit(account_txt,password_txt)
    def regis_button_enabled(self):
        account_txt=self.account_line.text()
        password_txt=self.password_line.text()
        confirm_txt=self.confirm_line.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(confirm_txt)>0 and password_txt==confirm_txt:
            self.regis_button.setEnabled(True)
        else:
            self.regis_button.setEnabled(False)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Register_jiemian()
    window.show()
    sys.exit(app.exec_())