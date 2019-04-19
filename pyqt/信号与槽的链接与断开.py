#QObject类中有两个自身带的信号一个是obj.destroyed()
import sys
from PyQt5.Qt import QApplication,QWidget,QObject
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        self.signal_slot()

    def signal_slot(self):
        obj=QObject()   #这个对象没人引用，或者说没有父控件，所以执行完一遍之后就被释放了，从而引发一个对象销毁的信号放射
        obj.destroyed.connect(self.destroy_cao)
        obj.objectNameChanged.connect(self.objectnamechange_cao)#注意这个执行在前，修改对象名字在后代码才能实现
        obj.setObjectName('hhh')
        obj.objectNameChanged.disconnect() #不影响信号发射，但是会中断与槽函数的链接和obj.blockSignals(True)执行的效果是一样的，还可以
        # 用print(obj.signalsBlocked())看信号是否被阻断
        print(obj.receivers(obj.objectNameChanged))#查看某个对象的中的某个信号连接着几个槽函数，注意括号中的参数

        obj.setObjectName('jjj')
    def destroy_cao(self,object): #这里是可以接收信号传过来的对象
        print(object,'对象被释放了')
    def objectnamechange_cao(self,name):#这里可以接收改的对象的名字
        print('对象名被改变成  ',name)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
