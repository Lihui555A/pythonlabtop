from PyQt5.Qt import QApplication,QWidget,QLineEdit
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        #输出模式设置
        line_1=QLineEdit(self)
        line_1.setEchoMode(1)#不输出 ，这里的不输出只是不显示，但是实际上是有内容的，可以用text()获取
        line_1.move(100,100)
        line_2 = QLineEdit(self)
        line_2.setEchoMode(0) #正常输出
        line_2.move(100, 200)
        line_3 = QLineEdit(self)
        line_3.setEchoMode(2)#密文形式
        line_3.move(100, 300)
        line_4 = QLineEdit(self)
        line_4.setEchoMode(3)#编辑时明文，结束后密文
        line_4.move(100, 400)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())