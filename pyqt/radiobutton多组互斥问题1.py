from PyQt5.Qt import QApplication,QWidget,QRadioButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        red = QWidget(self)
        red.resize(100, 100)
        red.move(100, 100)
        red.setStyleSheet('background-color:red')
        green = QWidget(self)
        green.resize(100, 100)
        green.move(300, 300)
        green.setStyleSheet('background-color:green')
        radiobutton_1=QRadioButton('男',red)
        radiobutton_2=QRadioButton('女',red)
        radiobutton_1.move(10,10)
        radiobutton_2.move(10,30)
        radiobutton_3 = QRadioButton('yes', green)
        radiobutton_4 = QRadioButton('no', green)
        radiobutton_3.move(30, 10)
        radiobutton_4.move(30, 30)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())