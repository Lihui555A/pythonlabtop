import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget,QPixmap,QCursor
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        lable=QLabel(self)
        lable.setText('hhh')
        self.lable=lable
        pixmap=QPixmap(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\noshadow\standart\bmp\24x24\001_02')
        pixmap=pixmap.scaled(10,10)
        cursor=QCursor(pixmap)
        self.setCursor(cursor)
        self.setMouseTracking(True)
    def mouseMoveEvent(self, QMouseEvent):
        self.lable.move(QMouseEvent.localPos().x(),QMouseEvent.localPos().y())#这里打印出的是鼠标的相对位置
    def enterEvent(self, QEvent):
        print('鼠标进来了')
    def leaveEvent(self, QEvent):
        print('鼠标出来了')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())