from PyQt5.Qt import QApplication,QWidget,QObject
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        self.QObject_parent_chil()
    def QObject_parent_chil(self):
        obj0=QObject()
        obj1=QObject()
        obj2=QObject()
        obj3=QObject()
        obj4=QObject()
        obj5=QObject()
        obj1.setParent(obj0)#设置父对象，一个对象只能有一个父对象，
        obj2.setParent(obj0)
        obj2.setObjectName('obj2')
        obj3.setParent(obj1)
        obj4.setParent(obj2)
        obj5.setParent(obj2)
        print(obj1.parent())
        print(obj0.children())#父对象用这种方法查找子对象只能查找一级，不能隔代查找
        print(obj0.findChild(QObject))#这样的方法只能用来查找一个子对象，括号里应该是三个参数分别是子对象的类名，属性名，第三个没用
        print(obj0.findChild(QObject,'obj2'))#这样的方法用来查找一个固定属性名的子对象，只要有属性名可以跨级查找
        print(obj0.findChildren(QObject))#可以查找所有的子对象，参数和上面的一样，也是三个
        #其实上面的代码最主要想说的就是pyqt中所有的空间对象都是直接或间接的继承自QObject类的，而这个类的实例是
        #可以设置父子关系的，也就是说在pyqt中任何空间都是可以设置父子关系的，其实说白了就是可以把一个控件（子对象）放在另一个控件（父对象）上，
        #就像一个窗口上放个按钮一样，当父对象被销毁的时候，子对象也会销毁，意思就是说界面关掉了，那么在这个界面上的所有的控件也就销毁了，不占内存了
        #所以说一旦一个子对象有附着在某个父对象上后，这个子对象的生命就有父对象接手了，只有父对象被释放的时候子对象才能释放
        #另外子对象的大小再大也不会超过父对象的大小
        obj1.destroyed.connect(lambda :print('obj1对象被释放了'))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())