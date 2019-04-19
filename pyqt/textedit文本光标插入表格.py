from PyQt5.Qt import QApplication,QWidget,QTextEdit,QPushButton,QTextTableFormat,Qt,QTextTable,QTextLength
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        line_1=QTextEdit(self)
        button=QPushButton(self)
        button.setText('我是按钮')
        button.move(400,100)
        button.clicked.connect(self.func)
        self.button=button
        self.line=line_1
    def func(self):
        textcursor=self.line.textCursor()
        ttf=QTextTableFormat()
        ttf.setAlignment(Qt.AlignCenter)
        ttf.setCellPadding(5)#单元格内边距
        ttf.setCellSpacing(10)#单元格外边距
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength,50),
                                       QTextLength(QTextLength.PercentageLength,40),
                                       QTextLength(QTextLength.PercentageLength,10)))#设置列宽度


        table=textcursor.insertTable(5,3,ttf)#返回的是个五行三列的表
        #table.appendColumns(2)#加两列

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())