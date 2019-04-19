from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys
class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo,self).__init__()
        label_1=QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)
        label_1.setText("这是一个文本标签")
        label_1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label_1.setPalette(palette)
        label_1.setAlignment(Qt.AlignCenter)


        label_2.setText('<a href="#">欢迎使用Python GUI应用</a>')
        label_3.setAlignment(Qt.AlignCenter)
        label_3.setToolTip('这是一个图片标签')
        label_3.setPixmap(QPixmap("1.jpg"))
        label_3.setFixedSize(300,500)
        label_4.setText('<A href="http://www.baidu.com">欢迎访问百度网站</a>')
        label_4.setAlignment(Qt.AlignRight)
        label_4.setToolTip('这是一个超链接标签')


        vbox=QVBoxLayout()
        vbox.addWidget(label_1)
        vbox.addStretch()
        vbox.addWidget(label_2)
        vbox.addStretch()
        vbox.addWidget(label_3)
        vbox.addStretch()
        vbox.addWidget(label_4)

        label_4.setOpenExternalLinks(True)
        label_2.setOpenExternalLinks(False)
        label_4.linkActivated.connect(self.link_clicked)
        label_2.linkHovered.connect(self.link_hovered)
        label_1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel例子')
    def link_hovered(self):
        print('当鼠标滑过label_2时发生事件')
    def link_clicked(self):
        print('当鼠标点击Label_4时发生事件')
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowDemo()
    win.show()
    sys.exit(app.exec_())
