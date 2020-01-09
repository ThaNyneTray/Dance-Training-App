from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
import sys, time
from code.dance_app_uis.modify_dance_window import Ui_ModifyDanceMove


def create_connection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("moves.sqlite")
    opened = db.open()
    if not opened:
        print(db.lastError().databaseText())
        print(db.lastError().driverText())
        print("database not found!")
        return

    return db


def initialize_model(model):
    model.setTable("moves")
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "Name")
    model.setHeaderData(1, Qt.Horizontal, "Category")
    model.setHeaderData(2, Qt.Horizontal, "Tags")
    model.setHeaderData(3, Qt.Horizontal, "Description")


def create_view(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


class ModifyDanceWindow(QtWidgets.QMainWindow):
    # init function
    def __init__(self):
        super(ModifyDanceWindow, self).__init__()
        self.ui = Ui_ModifyDanceMove()
        self.ui.setupUi(self)

        self.db = create_connection()

        self.model = QSqlTableModel(db=self.db)
        self.modelV2 = QSqlTableModel(db=self.db)
        initialize_model(self.modelV2)
        initialize_model(self.model)

        self.ui.moves_View.setModel(self.model)
        self.ui.moves_View.setSortingEnabled(True)
        self.ui.submit_Button.clicked.connect(self.push_to_db)
        self.ui.cancel_Button.clicked.connect(self.cancel_changes)
        self.ui.search_lineEdit.textChanged.connect(self.search)

    def push_to_db(self):
        # TODO: pop a confirmation dialog
        self.model.submitAll()

    def cancel_changes(self):
        self.model.revertAll()

    # Implementing search.
    # We take advantage of the qsqltable model - setFilter + filter_combobox
    def search(self):
        # we're using setFilter to implement search.
        pattern = self.ui.search_lineEdit.text()
        search_filter = self.ui.filter_comboBox.currentText()
        if pattern is None or pattern == "":
            self.model.setFilter("")
        elif search_filter == "Everything":
            self.model.setFilter(("name LIKE '%{0}%' "
                                  "OR category LIKE '%{0}%' "
                                  "OR tags LIKE '%{0}%'"
                                  "OR description LIKE '%{0}%'".format(pattern)))
        elif search_filter == "Name":
            self.model.setFilter(("name LIKE '%{0}%'".format(pattern)))
        elif search_filter == "Category":
            self.model.setFilter(("category LIKE '%{0}%'".format(pattern)))
        elif search_filter == "Tags":
            self.model.setFilter(("tags LIKE '%{0}%'".format(pattern)))
        elif search_filter == "Description":
            self.model.setFilter(("description LIKE '%{0}%'".format(pattern)))


app = QtWidgets.QApplication(sys.argv)
window = ModifyDanceWindow()
window.show()
app.exec_()
