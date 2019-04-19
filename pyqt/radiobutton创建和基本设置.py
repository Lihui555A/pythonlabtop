from PyQt5.Qt import QApplication,QWidget,QRadioButton,QIcon,QSize
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        radiobutton_1=QRadioButton('男',self)
        radiobutton_2=QRadioButton('女',self)
        radiobutton_2.setIcon(QIcon(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\noshadow\standart\bmp\24x24\001_01.bmp'))
        radiobutton_2.setIconSize(QSize(20,20))
        radiobutton_2.move(200,200)
        radiobutton_2.setChecked(True)#默认自动选中
        radiobutton_2.setShortcut('Alt+M') #设置快捷键
        #常用信号
        #radiobutton_2.pressed()
        radiobutton_2.toggled.connect(lambda :print('hehehe'))



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())