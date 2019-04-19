import sys
from PyQt5.Qt import QApplication,QLabel,QPushButton,QWidget
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.resize(500,500)
    def setup_ui(self):
        label=QLabel(self)
        label.setText('h')
        label.move(100,100)
        self.label=label
        button=QPushButton(self)
        button.setText('点我')
        button.move(200,200)
        button.clicked.connect(self.pro_long)
    def pro_long(self):
        text=self.label.text()
        self.label.setText(text+'h')
        self.label.adjustSize()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Widget()
    window.show()
    sys.exit(app.exec_())

