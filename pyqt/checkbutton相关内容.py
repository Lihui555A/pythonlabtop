from PyQt5.Qt import QApplication,QWidget,QRadioButton,QCheckBox,Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        checkbox_1=QCheckBox('男',self)
        checkbox_2=QCheckBox('女',self)
        checkbox_1.move(100,100)
        checkbox_2.move(200,200)
        checkbox_1.setTristate(True)#用来设置三态
        checkbox_1.setCheckState(Qt.Unchecked)#未被选中
        checkbox_1.setCheckState(Qt.PartiallyChecked)  # 部分选中
        checkbox_1.setCheckState(Qt.Checked)  # 真的被选中
        #独有信号
        checkbox_1.stateChanged.connect(lambda state:print(state)) #这里发射信号的时候会把状态发射出来，未被选中的状态发射数字0，半选中状态发射数字1，完全选中状态发射数字2
        checkbox_1.stateChanged.connect(lambda :print('信号被选中'))




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())