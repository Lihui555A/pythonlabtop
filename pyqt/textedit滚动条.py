from PyQt5.Qt import QApplication,QWidget,QTextEdit,Qt,QPushButton,QIcon
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        button=QPushButton(self)
        button.setIcon(QIcon(r'C:\Users\lihui\Desktop\python文件\Icon\beautiful\noshadow\standart\ico\001_01.ico'))
        line_1=QTextEdit(self)
        line_1.setText('斤斤计较 ')
        # line_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)#设置水平滚动条，并且保持始终开启,M默认是关闭的
        # line_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)#设置垂直滚动条，默认是开启的，

        line_1.setCornerWidget(button)
        print(line_1.toPlainText()) #获取文本
        line_1.insertPlainText('ddddd')#在光标处插入文本
        line_1.append('dfsfsdf')#在文本内容的后边增加文本





if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())