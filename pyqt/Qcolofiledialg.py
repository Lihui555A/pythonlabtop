from PyQt5.Qt import QApplication,QWidget,QLabel,QColorDialog,QPushButton,QPalette
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QLabel(self)
        line_1.setText('实例文字')
        self.line_1=line_1
        button=QPushButton(self)
        button.setText('改变字体颜色')
        button.move(200,200)
        button.clicked.connect(self.color_change)
        self.color = QColorDialog(self)
        self.color.colorSelected.connect(self.color_changge)
    def color_change(self):
        self.color.show()
    def color_changge(self,color):
        palette = QPalette()
        palette.setColor(QPalette.Foreground, color)
        self.line_1.setPalette(palette)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())