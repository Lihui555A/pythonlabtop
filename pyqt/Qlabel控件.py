from PyQt5.Qt import QApplication,QWidget,QLabel,QPixmap
from PyQt5.QtCore import Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLabel(self)
        # line_1.setText('我是标签dfsfsdfsfsdfsdfsfs')
        # line_1.adjustSize()
        # line_1.setAlignment(Qt.AlignRight)#设置文本对齐方式
        # line_1.setIndent(20)#在对齐的那一边设置缩进
        # line_1.setMargin(20)#设置内容区域到边框的距离，上下左右
        line_1.setPixmap(QPixmap(r'C:\Users\lihui\Desktop\python文件\pyqt\1.jpg.'))
        line_1.setScaledContents(True)
        line_2=QLabel(self)
        line_2.setText('<a href="http://www.baidu.com">百度</a>')
        line_2.setOpenExternalLinks(True)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())