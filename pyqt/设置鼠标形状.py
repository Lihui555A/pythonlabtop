import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget,Qt
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        self.setCursor(Qt.PointingHandCursor)#到时候换成不同的枚举值就可以了
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())