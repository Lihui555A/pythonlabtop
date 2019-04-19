from PyQt5.Qt import QApplication,QWidget,QLabel,QMovie
from PyQt5.QtCore import QSize,pyqtSignal,QPropertyAnimation,QPoint,QAbstractAnimation
from 复杂界面重复.zhuce import Ui_Form
import sys
class zhuce(QWidget,Ui_Form):
    show_denglu_pane_signal=pyqtSignal()
    login_button_clicked_signal=pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        movie=QMovie(":/image/1.gif")
        movie.setScaledSize(QSize(460,212))
        self.donghua_lable.setMovie(movie)
        movie.start()
        print(self.donghua_lable.size())
    def show_denglu_pane(self):
        self.show_denglu_pane_signal.emit()
    def denglu_button_ennable(self):
        zhanghao=self.comboBox.currentText()
        mima=self.lineEdit.text()
        if len(zhanghao)>0 and len(mima)>0:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)
    def zidongdenglu_button_clicked(self,checked):
        if checked:
            self.checkBox_2.setChecked(True)
    def jizhumima_button_clicked(self,checked):
        if not checked:
            self.checkBox.setChecked(False)

    def login_button_clicked(self):
        zhanghao=self.comboBox.currentText()
        mima=self.lineEdit.text()
        self.login_button_clicked_signal.emit(zhanghao,mima)
    def show_error_animation(self):
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self.widget_2)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0,self.widget_2.pos())
        animation.setKeyValueAt(0.2, self.widget_2.pos()+QPoint(15,0))
        animation.setKeyValueAt(0.5, self.widget_2.pos())
        animation.setKeyValueAt(0.7, self.widget_2.pos()+QPoint(-15,0))
        animation.setKeyValueAt(1, self.widget_2.pos())
        animation.setDuration(100)
        animation.setLoopCount(300)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=zhuce()
    window.show()
    sys.exit(app.exec_())