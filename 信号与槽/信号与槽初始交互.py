
from PyQt5.QtCore import *

class mysignal(QObject):
    signal=pyqtSignal(str)
    def run(self):
        self.signal.emit('nihao')
class myslot(QObject):
    def get(self,str):
        print(str)
if __name__ == '__main__':
    mys=mysignal()
    myc=myslot()
    mys.signal.connect(myc.get)
    mys.run()