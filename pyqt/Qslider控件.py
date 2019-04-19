import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SliderDemo(QWidget):
    def __init__(self,parent=None):
        super(SliderDemo, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QSlider例子')
        self.resize(300,100)

        #垂直布局
        layout=QVBoxLayout()

        #创建标签，居中
        self.l1=QLabel('Hello PyQt5')
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
        #创建水平方向滑动条
        self.s1=QSlider(Qt.Horizontal)
        ##设置最小值
        self.s1.setMinimum(10)
        #设置最大值
        self.s1.setMaximum(50)
        #步长
        self.s1.setSingleStep(3)
        #设置当前值
        self.s1.setValue(20)
        #刻度位置，刻度下方
        self.s1.setTickPosition(QSlider.TicksBelow)
        #设置刻度间距
        self.s1.setTickInterval(5)
        layout.addWidget(self.s1)
        #设置连接信号槽函数
        self.s1.valueChanged.connect(self.valuechange)

        self.setLayout(layout)

    def valuechange(self):
        #输出当前地刻度值，利用刻度值来调节字体大小
        print('current slider value=%s'%self.s1.value())
        size=self.s1.value()
        self.l1.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=SliderDemo()
    demo.show()
    sys.exit(app.exec_())
