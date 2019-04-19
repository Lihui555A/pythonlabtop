from PyQt5.Qt import QApplication,QWidget,QLabel,QPushButton
from PyQt5.QtCore import QObject
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        self.label=mylabel(self)
        self.label.setText('10')
        self.label.move(100,100)
        self.button=QPushButton(self)
        self.button.setText('开始倒计时')
        self.button.move(200,200)
        self.button.clicked.connect(self.func)
    def func(self):
        if self.button.text()=='开始倒计时':
            self.label_id=self.label.startTimer(1000)
            self.button.setText('停止倒计时')
        else:
            self.label.killTimer(self.label_id)
            self.button.setText('开始倒计时')
class mylabel(QLabel):
    def timerEvent(self, *args, **kwargs):
        text=self.text()
        if text=='0':
            return
        newtext=str(int(text)-1)
        self.setText(newtext)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())