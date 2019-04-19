# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel  # 表模型
from PyQt5.QtCore import Qt
def initializeModel(model):
    model.setTable('user') #这里必须得写数据库里表的名字
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "name")
    model.setHeaderData(2, Qt.Horizontal, "address")
def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view
def addrow():
    ret = model.insertRows(model.rowCount(), 1)
    print('insertRows=%s' % str(ret))
def findrow(i):
    delrow = i.row()#出来的是点击的那一行的索引
    colum=i.column()#出来的是那一列的索引
    print('del row=%s ' % str(delrow) )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('database.db')
    model = QSqlTableModel()  # 实例化一个表模型
    delrow = -1
    initializeModel(model)  #初始化模型
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)#每次点击会发射一个信号，这个信号会返回点击那一个点的行和列的索引

    dlg = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view1)
    addBtn = QPushButton("添加一行")
    addBtn.clicked.connect(addrow)
    layout.addWidget(addBtn)

    delBtn = QPushButton("删除一行")
    delBtn.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(delBtn)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database 例子")
    dlg.resize(430, 450)
    dlg.show()
    sys.exit(app.exec_())

#窗口控件上放tablewidget,然后在tablewidget上放模型，模型从数据库里拿数据，在表格上的操作都是操作模型的一些方法


