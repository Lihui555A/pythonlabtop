#这里需要注意的就是以后每一个控件上都要写上id然后呢用app去调用qss文件，在qss文件中全部用#id名字去设置样式
#这样的话即使是父控件，，修改的也只是自己本身，不会去改变父控件身上的子控件的样式
#但是在代码中如果用某个父控件去调用样式方法的话，这个样式方法的调用级别是比app去调用级别要高，而且父控件上的子控件会受影响



from PyQt5.Qt import QApplication,QWidget,QCheckBox
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        checkbox=QCheckBox(self)
        checkbox.setText('点击选中我')
        checkbox.setObjectName('checkbox')




if __name__ == '__main__':
    app=QApplication(sys.argv)
    with open('CheckBox.qss')as f:
        app.setStyleSheet(f.read())
    window=Window()
    window.show()
    sys.exit(app.exec_())