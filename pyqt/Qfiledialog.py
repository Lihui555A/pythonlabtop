from PyQt5.Qt import QApplication,QWidget,QTextEdit,QFileDialog,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
        self.button=QPushButton('点击打开文件夹路径',self)
        self.button.move(100,100)
        self.button.clicked.connect(self.open_file)
        self.button_1 = QPushButton('点击打开文件路径', self)
        self.button_1.move(200, 100)
        self.button_1.clicked.connect(self.open_directory)
    def setip_ui(self):
        self.resize(500, 500)

    def open_directory(self):
        # 父控件  对话框标题    开始目录  过滤文件类型                                        打开时展示文件类型
        # result=QFileDialog.getOpenFileName(self,'选择一个py文件','./','ALL(*.*);;images(*.png *.jpg);;Python文件(*.py)','Python文件(*.p)')#获得一个文件的绝对路径
        # result=QFileDialog.getOpenFileNames(self,'选择一个py文件','./','ALL(*.*);;images(*.png *.jpg);;Python文件(*.py)','Python文件(*.p)')#获取多个文件的绝对路径按住control来操作
        result = QFileDialog.getSaveFileName(self, '选择一个py文件', './', 'ALL(*.*);;images(*.png *.jpg);;Python文件(*.py)',
                                             'Python文件(*.p)')  # 获取想要储存的文件路径
        print(result)
    def open_file(self):
        result=QFileDialog.getExistingDirectory(self, '选择一个py文件', './')
        print(result)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())