from PyQt5.Qt import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        box_1=QWidget(self)
        box_2=QWidget(self)                                          #在自身上找到PushButton这样一个控件对象
        #box_1.setStyleSheet('QPushButton {background-color:red}') #用选择器来限定自己身上的子控件的样式
        #box_2.setStyleSheet('background-color:blue')#一个控件自己去调用setstylesheet方法，改变的是本身，和自己身上其他的子控件
        layout=QVBoxLayout()
        self.setLayout(layout)

        line_1=QLabel(box_1)
        line_1.setText('我是标签一')
        button_1=QPushButton(box_1)
        button_1.setText('我是按钮一')
        button_1.move(100,100)

        line_2 = QLabel(box_2)
        line_2.setText('我是标签er')
        button_2 = QPushButton(box_2)
        button_2.setText('我是按钮er')
        button_2.move(100, 100)
        layout.addWidget(box_1)
        layout.addWidget(box_2)
        #self.setStyleSheet('QPushButton {background-color:red}')  # 这里是在全局的布局上设置某个特定对象的样式
        self.button_3=QPushButton()                                   #这里有一种特殊情况就是，self，setstylesheep是指在这个主窗口上所有的指定的类别控件进行样式修改
        self.button_3.show()                                           #比如像这个同行的代码就是开启一个新的窗口，在这个窗口上的按钮控件是不受影响的



if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyleSheet('QPushButton {background-color:red}')#这里是在全局的布局上设置某个特定对象的样式
    window=Window()                                           #运行这句话的话会使得整个跟整个应用程序有关的所有的窗口上的制定控件都受影响，包括新开的窗口上的控件也会受到影响
    window.show()
    sys.exit(app.exec_())