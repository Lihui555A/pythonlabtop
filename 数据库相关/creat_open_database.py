import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')  # 添加数据库引擎
    db.setDatabaseName('database.db')  # 设置数据库名称

    if not db.open():
        QMessageBox.critical(None, ("无法打开数据库"),
                             ("无法建立到数据库的连接,这个例子需要SQLite 支持，请检查数据库配置。\n\n"
                              "点击取消按钮退出应用。"),
                             QMessageBox.Cancel)
        return False
    query = QSqlQuery()  # 建立一个数据库写手
    query.exec_("create table user(id int primary key, account varchar(20), password int)")
    query.exec_("create table car(id int primary key, picture_name varchar(100),car_type varchar(200),detect_time varchar(30),after_detect_picture_path varchar(100) )")
    query.exec_("insert into user values(1, 'zhangsan1', 1)")
    query.exec_("insert into user values(2, 'lisi1', 2)")
    query.exec_("insert into user values(3, 'wangwu1', 3)")
    query.exec_("insert into user values(4, 'lisi2', 4)")
    query.exec_("insert into user values(5, 'wangwu2', 5)")
    db.close()
    return True

if __name__ == '__main__':

    createDB()

