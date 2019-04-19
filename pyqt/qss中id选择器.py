#这里需要注意的就是以后每一个控件上都要写上id然后呢用app去调用qss文件，在qss文件中全部用#id名字去设置样式
#这样的话即使是父控件，，修改的也只是自己本身，不会去改变父控件身上的子控件的样式
#但是在代码中如果用某个父控件去调用样式方法的话，这个样式方法的调用级别是比app去调用级别要高，而且父控件上的子控件会受影响



from PyQt5.Qt import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        box_1=QWidget(self)
        box_1.setObjectName('box_1')
        box_2 = QWidget(self)
        box_2.setObjectName('box_2')
        #box_2.setStyleSheet('background-color:blue')
        #box_1.setStyleSheet('#button_3 {background-color:red}')  # 用Id选择器来限定自己身上的子控件的样式

        button_3 = QPushButton(box_1)
        button_3.setText('我是按钮三')
        button_3.move(100, 200)
        button_3.setObjectName('button_3')



       #一个控件自己去调用setstylesheet方法，改变的是本身，和自己身上其他的子控件
        line_1 = QLabel(box_1)
        line_1.setText('我是标签一')
        line_1.setObjectName('label_1')
        button_1 = QPushButton(box_1)
        button_1.setText('我是按钮一')
        button_1.move(100, 100)
        button_1.setObjectName('button_1')

        line_2 = QLabel(box_2)
        line_2.setText('我是标签er')
        line_2.setObjectName('label_2')
        button_2 = QPushButton(box_2)
        button_2.setText('我是按钮er')
        button_2.move(100, 100)
        button_2.setObjectName('button_2')
        button_2.setProperty('level','error')


        layout=QVBoxLayout()
        self.setLayout(layout)


        layout.addWidget(box_1)
        layout.addWidget(box_2)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    with open('buttonlabel.qss')as f:
        app.setStyleSheet(f.read())
    window=Window()
    window.show()
    sys.exit(app.exec_())