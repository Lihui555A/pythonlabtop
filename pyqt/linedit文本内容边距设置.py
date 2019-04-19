from PyQt5.Qt import QApplication,QWidget,QLineEdit,QValidator
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        line_1.move(100,100)
        line_1.setMaxLength(3)#设置允许输入最多字符个数
        line_2 = QLineEdit(self)
        line_2.move(100, 200)
        line_2.setReadOnly(True)#设置只读模式
        line_3 = QLineEdit(self)
        line_3.move(100, 300)

        line_4 = QLineEdit(self)
        line_4.move(100, 400)
        line_4.setTextMargins(10,0,0,0)#设置标签空间的文本边距，上左下右



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())