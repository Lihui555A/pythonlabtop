from PyQt5.Qt import QApplication,QWidget,QRadioButton,QButtonGroup
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500, 500)
        buttongroup = QButtonGroup(self)

        radiobutton_1 = QRadioButton('男', self)
        radiobutton_2 = QRadioButton('女', self)
        radiobutton_2.setChecked(True)  # 设置默认选中
        radiobutton_1.move(10, 10)
        radiobutton_2.move(10, 30)
        buttongroup.addButton(radiobutton_1, 1)  # 括号中的后一个参数表示的是给添加到这个组的某个按钮设置一个相对于这个组中的id
        buttongroup.addButton(radiobutton_2)
        radiobutton_3 = QRadioButton('yes', self)
        radiobutton_4 = QRadioButton('no', self)
        radiobutton_3.move(90, 10)
        radiobutton_4.move(90, 30)
        buttongroup.setId(radiobutton_1,1)
        buttongroup.setId(radiobutton_2,2)
        buttongroup.buttonToggled.connect(self.button_clickde)#按钮组中的按钮发生状态发生改变的时候会发射这个信号，这个信号中会传递两个参数，一个是状态发生改变的控件，还有一个是状态发生改变的控件的id
        buttongroup.buttonClicked[int].connect(self.button_clickd)#这个是发射按钮组中被点击的按钮的id
        buttongroup.buttonClicked.connect(self.button_click)  # 这个是发射按钮组中被点击的按钮的控件
    def button_clickde(self,widget):
        print(widget)
    def button_clickd(self,id):
        print(id)
    def button_click(self,widget):
        print(widget)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())