import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget,Qt,QCursor,QPixmap
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()
    def setup_ui(self):
        pixmap=QPixmap(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\shadow\grey\bmp\24x24\001_01')
        pixmap=pixmap.scaled(10,10)#这里是鼠标图标大小
        cursur=QCursor(pixmap,10,10)#这个括号里的后两个参数可以不写，表示的鼠标的有效点位置，默认情况下是图片的中间
        self.setCursor(cursur)
        self.cursor=cursur
       # self.unsetCursor()#这句话的意思是取消鼠标重置
        print(self.cursor.pos())#打印鼠标位置，相对于电脑屏幕的左上角
        self.cursor.setPos(0,0)#设置鼠标位置
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())