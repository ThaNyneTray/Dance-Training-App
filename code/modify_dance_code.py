from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QItemSelectionModel
from PyQt5.QtSql import *
import sys
from code.dance_app_uis.modify_dance_window import Ui_ModifyDanceMove
from code.add_dance_code import *
import code.database_manager as database_manager


# TODO: move this to a separate file??
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
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


class ModifyDanceWindow(QMainWindow):
    # init function
    def __init__(self):
        super(ModifyDanceWindow, self).__init__()
        self.ui = Ui_ModifyDanceMove()
        self.ui.setupUi(self)

        self.db = create_connection()

        self.model = QSqlTableModel(db=self.db)
        initialize_model(self.model)

        self.ui.moves_View.setModel(self.model)
        self.ui.moves_View.hideColumn(2)
        self.ui.moves_View.hideColumn(3)
        self.ui.moves_View.setSortingEnabled(True)
        self.ui.moves_View.resizeColumnsToContents()
        self.ui.moves_View.horizontalHeader().setStretchLastSection(True)
        self.ui.moves_View.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.moves_View.selectionModel().selectionChanged.connect(self.populate_dance_data_fields)
        self.ui.submit_Button.clicked.connect(self.push_to_db)
        self.ui.cancel_Button.clicked.connect(self.cancel_changes)
        self.ui.search_lineEdit.textChanged.connect(self.search)

    def populate_dance_data_fields(self):
        category_indexes = {"Technique/Step": 0, "Concept": 1, "Set": 2, "Choreography": 3}
        selected_indexes = self.ui.moves_View.selectedIndexes()
        if not selected_indexes:
            return
        selected_move_attribute = selected_indexes[0].data()
        selected_move = dance_moves[selected_move_attribute]
        print(selected_move.name, selected_move.description, selected_move.tags, selected_move.category)
        self.ui.name_lineEdit.setText(selected_move.name)
        self.ui.description_textEdit.setText(selected_move.description)
        self.ui.category_comboBox.setCurrentIndex(category_indexes[selected_move.category])

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


app = QApplication(sys.argv)
modify_dance_window = ModifyDanceWindow()
# window.show()
# app.exec_()
