from PyQt5.Qt import QApplication,QWidget,QLineEdit,QPushButton
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        line_1.move(100,100)
        line_2 = QLineEdit(self)
        line_2.move(200,200)
        button=QPushButton(self)
        button.setText('复制')
        button.move(300,300)
        button.clicked.connect(self.copy)
        self.line_1=line_1
        self.line_2=line_2
    def copy(self):
        text=self.line_1.text()
        self.line_2.setText(text)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())