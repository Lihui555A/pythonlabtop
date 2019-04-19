from PyQt5.Qt import QApplication,QWidget,QLabel
from PyQt5.QtCore import QThread,pyqtSignal,QDateTime
import sys
import time
class Time_display(QThread):
    time_change_signal=pyqtSignal(str)
    def __init__(self):
        super(Time_display, self).__init__()
    def run(self):
        while  True:
            data=QDateTime.currentDateTime()
            currentTime=data.toString('yyyy-MM-dd hh:mm:ss')
            self.time_change_signal.emit(currentTime)
            time.sleep(1)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        self.lable=QLabel(self)

        self.lable.move(100,100)
        self.time_change=Time_display()
        self.time_change.time_change_signal.connect(self.time_change_func) #记着这里是有参数传递的
        self.time_change.start()
    def time_change_func(self,str):#槽函数记得接受参数
        self.lable.setText(str)
        self.lable.adjustSize()





if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())