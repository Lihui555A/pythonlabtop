from PyQt5.QtCore import QDate,   QDateTime , QTime
from PyQt5.Qt import QApplication,QWidget,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        button=QPushButton(self)
        button.setText('计时开始')
        button.clicked.connect(self.start)
    def start(self):
        time=QTime.currentTime()
        time.start()
        print(time.elapsed())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
