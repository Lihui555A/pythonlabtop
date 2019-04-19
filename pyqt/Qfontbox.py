from PyQt5.Qt import QApplication,QWidget,QTextEdit,QFontComboBox
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QTextEdit(self)
        line_1.setText('好好学习，天天向上')
        line_1.move(100,100)
        fcb=QFontComboBox(self)
        fcb.resize(200,20)
        fcb.setEditable(False)
        fcb.currentFontChanged.connect(lambda font:line_1.setFont(font))




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())