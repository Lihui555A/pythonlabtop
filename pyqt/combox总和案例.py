from PyQt5.Qt import QApplication,QWidget,QComboBox
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.data={'北京':{'东城':'001','西城':'002','朝阳':'003','丰台':'004'}
                      ,'上海':{'黄浦':'005','徐汇':'006','长宁':'007','静安':'008','松江':'009'}
                      ,'广东':{'广州':'010','深圳':'011','湛江':'012','佛山':'013','海南':'014'}}
        self.setip_ui()
    def setip_ui(self):
        self.resize(500,500)
        com_1=QComboBox(self)
        com_2=QComboBox(self)
        com_1.move(100,100)
        com_2.move(200,100)
        self.com_2 = com_2
        self.com_1 = com_1
        self.com_2.currentIndexChanged[int].connect(self.com_2_changge)
        self.com_1.currentIndexChanged[str].connect(self.com_1_changge)
        self.com_1.addItems(self.data.keys())  # 开始时直接把省份的名字放到空间一上面

    def com_1_changge(self,name):
        self.com_2.blockSignals(True)
        self.com_2.clear()
        self.com_2.blockSignals(False)
        for key,value in self.data[name].items():
            self.com_2.addItem(key,value)

    def com_2_changge(self,index):
        print(self.com_2.itemData(index))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())