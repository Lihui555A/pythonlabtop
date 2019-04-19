import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget,Qt
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
        self.setMouseTracking(True)
    def setup_ui(self):
        self.setCursor(Qt.PointingHandCursor)#到时候换成不同的枚举值就可以了
    def mouseMoveEvent(self, QMouseEvent):
        print('haha')#正常来说只要鼠标放在这个空间上然后移动就会触发这个事件，但是这个没有，因为有一个开关没打
        # 开，把这个开关打开，就是这句话self.setMouseTracking(True)然后在控件上移动鼠标就有反应了，
        #如果不想打开开关，想要有反应就得按下鼠标左键然后进行移动
        print(QMouseEvent.globalPos())#打印鼠标位置

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())