from PyQt5.Qt import QApplication,QWidget,QLineEdit,QCompleter
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLineEdit(self)
        completer=QCompleter(['sss','sdf','hhh','hjk'],line_1)
        line_1.setCompleter(completer)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())