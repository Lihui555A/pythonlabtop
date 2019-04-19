from PyQt5.Qt import QApplication,QWidget
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel
from PyQt5.QtCore import Qt
import sys
from 数据库相关.use_tableview_control_databese_bymyself import Ui_Form
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        self.model=QSqlTableModel()
        self.init_model(self.model)
        self.tableView.setModel(self.model)
    def init_model(self,model):
        model.setTable('user')  # 这里必须得写数据库里表的名字
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "name")
        model.setHeaderData(2, Qt.Horizontal, "address")
    def add_row(self):
        if self.tableView.currentIndex().row()>=0:
            self.model.insertRows(self.tableView.currentIndex().row()+1,1)#这个里边的参数是要添加的索引
        else:
            self.model.insertRows(self.model.rowCount(),1)
    def sub_row(self):
        self.model.removeRows(self.tableView.currentIndex().row(), 1)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mywin=Mywin()
    mywin.show()
    sys.exit(app.exec_())

