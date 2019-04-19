from PyQt5.Qt import QApplication,QWidget,QRadioButton,QButtonGroup
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        buttongroup=QButtonGroup(self)

        radiobutton_1=QRadioButton('男',self)
        radiobutton_2=QRadioButton('女',self)
        radiobutton_2.setChecked(True)#设置默认选中
        radiobutton_1.move(10,10)
        radiobutton_2.move(10,30)
        buttongroup.addButton(radiobutton_1,1)#括号中的后一个参数表示的是给添加到这个组的某个按钮设置一个相对于这个组中的id
        buttongroup.addButton(radiobutton_2)
        radiobutton_3 = QRadioButton('yes', self)
        radiobutton_4 = QRadioButton('no', self)
        radiobutton_3.move(90, 10)
        radiobutton_4.move(90, 30)
        print(buttongroup.buttons()) #查看某个按钮组中的所有按钮控件
        print(buttongroup.button(1)) #根据按钮组中的id,查看某个按钮组的某个控件，
        print(buttongroup.checkedButton())#查看组中已经被选中的按钮

        #buttongroup.removeButton(radiobutton_2)#移出按钮只是从组中删除，并不从界面上删除
        #给按钮组中的按钮控件设置id
        buttongroup.setId(radiobutton_1,1)
        buttongroup.setId(radiobutton_2,2)
        print(buttongroup.id(radiobutton_2))#获取按钮组中的某个按钮的id
        print(buttongroup.checkedId())#获取按钮组中的选中的按钮的id,如果没有选中的，返回—1
        buttongroup.setExclusive(False)#设置按钮组中的按钮的互斥情况


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())