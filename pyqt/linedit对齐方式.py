from PyQt5.Qt import QApplication,QWidget,QLineEdit,Qt
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500, 500)
        line_1 = QLineEdit(self)
        line_1.move(100, 100)

        line_1.setAlignment(Qt.AlignRight)#设置文本内容在控件的右边
        line_2 = QLineEdit(self)
        line_2.move(100, 200)
        line_2.setAlignment(Qt.AlignBottom)#如果控件大一点的话，会在控件的下面
        line_3 = QLineEdit(self)
        line_3.move(100, 300)
        line_3.setAlignment(Qt.AlignCenter)#内容在中间
        line_4 = QLineEdit(self)
        line_4.move(100, 400)
        line_1.setAlignment(Qt.AlignRight|Qt.AlignBottom)#内容在右下角




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())