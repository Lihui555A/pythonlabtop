from PyQt5.Qt import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        box_1=QWidget(self)
        box_2=QWidget(self)
        box_1.setStyleSheet('background-color:red') #样式表不同的调用方式会影响父控件里的子控件的样式
        box_2.setStyleSheet('background-color:blue')#一个控件自己去调用setstylesheet方法，改变的是本身，和自己身上其他的子控件
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

#对于想设置某个具体的单个控件，只需要用控件本身去设定样式就可以了
#相对一个父控件上的某些相同类型的控件进行样式控制，就得用这个父控件去调用方法，但是方法内部要标明要修改的控件的类别，
#这样的话这个父控件的上的某个类别的所有的控件就都会进行相应的修改
#如果想对父控件上的某个特定的控件进行样式设定，就得用父控件去调用方法，但是在语句中既要规定控件类型，又有规定控件的id

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())