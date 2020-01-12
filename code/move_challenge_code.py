from PyQt5 import QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
from code.dance_app_uis.move_challenge_window import Ui_ChallengeWindow


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
    # model.selectStatement
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "Name")


class MoveSelectWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MoveSelectWindow, self).__init__()
        self.ui = Ui_ChallengeWindow()
        self.ui.setupUi(self)
        self.attach_slots()
        self.init_db()

        self.db = create_connection()

        self.model = QSqlTableModel(db=self.db)
        initialize_model(self.model)

        # setting up the from/left list view
        self.ui.from_listView.setModel(self.model)
        self.ui.from_listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.from_listView.setSelectionRectVisible(False)
        self.ui.from_listView.setFocusPolicy(Qt.NoFocus)

        # setting up the to/right list view
        self.ui.to_listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.to_listView.setSelectionRectVisible(False)
        self.ui.to_listView.setFocusPolicy(Qt.NoFocus)

    def attach_slots(self):
        # attach the Add and Remove buttons to respective signals
        self.ui.add_pushButton.clicked.connect(self.add)
        self.ui.remove_pushButton.clicked.connect(self.remove)
        self.ui.next_pushButton.clicked.connect(self.open_challenge_window)

    def init_db(self):
        pass

    # TODO: surely there's a better way to do this. Please revisit as you gain experience with PyQT
    # function to retrieve data already present
    def get_old_items(self):
        first_index = self.ui.to_listView.indexAt(QPoint(0, 0))
        old_entries = set()
        if first_index.isValid():
            old_entries = {first_index.data()}
            next_index = self.ui.to_listView.visualRect(first_index).y() \
                         + self.ui.to_listView.visualRect(first_index).height() + 1
            while self.ui.to_listView.indexAt(QPoint(0, next_index)).isValid():
                first_index = self.ui.to_listView.indexAt(QPoint(0, next_index))
                old_entries.add(first_index.data())
                next_index = self.ui.to_listView.visualRect(first_index).y() \
                             + self.ui.to_listView.visualRect(first_index).height() + 1
        return old_entries

    # function to update data on the to listview
    def add(self):
        old_entries = self.get_old_items()
        new_entries = (each.data() for each in self.ui.from_listView.selectedIndexes())
        entries = old_entries.union(new_entries)
        model = QStandardItemModel()
        self.ui.to_listView.setModel(model)
        for each in entries:
            item = QStandardItem(each)
            model.appendRow(item)

    # function to remove data from the to listview
    def remove(self):
        old_entries = self.get_old_items()
        indexes_to_remove = (each.data() for each in self.ui.to_listView.selectedIndexes())

        entries = old_entries.difference(indexes_to_remove)
        model = QStandardItemModel()
        self.ui.to_listView.setModel(model)
        for each in entries:
            item = QStandardItem(each)
            model.appendRow(item)

    # def repopulate(self):
    #     pass

    # slot/method to open the challenge window
    def open_challenge_window(self):
        window.hide()
        suggest_window = msc.MoveChallengeWindow()
        suggest_window.show()


import code.move_suggest_code as msc

_excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    _excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QtWidgets.QApplication(sys.argv)
window = MoveSelectWindow()
window.show()
app.exec_()
