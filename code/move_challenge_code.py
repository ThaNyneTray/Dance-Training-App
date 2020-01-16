import sys
import random
import threading
import time
from PyQt5 import QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from code.dance_app_uis.move_challenge_window import Ui_ChallengeWindow
from code.dance_app_uis.move_suggest_window import Ui_MoveChallengeWindow


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
        select_window.hide()
        challenge_window.show()


class MoveChallengeWindow(QtWidgets.QMainWindow):
    # init function
    def __init__(self):
        super(MoveChallengeWindow, self).__init__()
        self.ui = Ui_MoveChallengeWindow()
        self.ui.setupUi(self)

        self.attach_slots()

        self.moves = None
        self.counter = 0

    def attach_slots(self):
        self.ui.time_slider.valueChanged.connect(lambda: self.val_changed(self.ui.time_slider, "lineEdit"))
        self.ui.time_lineEdit.textChanged.connect(lambda: self.val_changed(self.ui.time_lineEdit, "slider"))
        self.ui.reset_pushButton.clicked.connect(self.reset)
        self.ui.start_pushButton.clicked.connect(self.start_suggestions)
        self.ui.pause_pushButton.clicked.connect(self.pause_suggestions)
        self.ui.stop_pushButton.clicked.connect(self.stop_suggestions)
        self.ui.change_pushButton.clicked.connect(self.open_moves_selection)

    # slot/method that links the slider with the line edit
    def val_changed(self, which, string):
        if not self.ui.time_lineEdit.text():
            return
        elif string == "lineEdit":
            self.ui.time_lineEdit.setText(str(self.ui.time_slider.value()))
        elif string == "slider":
            self.ui.time_slider.setValue(int(self.ui.time_lineEdit.text()))

    # slot/method for reset button
    def reset(self):
        self.ui.time_lineEdit.setText("8")
        self.ui.time_slider.setValue(8)

    # slot/method for start button. this creates a thread that changes the moves
    #  label every x seconds.
    def start_suggestions(self):
        self.moves = list(select_window.get_old_items())
        if self.ui.start_pushButton.text() == "Start":
            self.ui.start_pushButton.setText("Restart")
            random.shuffle(self.moves)
        elif self.ui.start_pushButton.text() == "Restart":
            self.counter = 0
            self.ui.pause_pushButton.setText("Pause")

        self.ui.pause_pushButton.setDisabled(False)
        suggestions_thread = threading.Thread(target=self.start_suggestions_event, daemon=True)
        suggestions_thread.start()

    def start_suggestions_event(self):
        # self.suggestions_thread = threading.Thread(target=self.suggestions_thread, daemon=True)
        # self.suggestions_thread.start()
        self.sugestions_event = threading.Event()
        self.interval = self.ui.time_slider.value()
        print(self.moves)
        while not self.sugestions_event.is_set() and self.counter < len(self.moves):
            print(self.counter, self.moves[self.counter])
            self.ui.move_label.setText(self.moves[self.counter])
            self.sugestions_event.wait(self.interval)
            self.counter += 1
            # if self.counter == len(self.moves):
            #     self.counter == 0
        # self.ui.move_label.setText("Moves list completed. \nClick start to restart.")

    def pause_suggestions(self):
        if self.ui.pause_pushButton.text() == "Pause":
            self.sugestions_event.set()
            self.ui.pause_pushButton.setText("Resume")
        elif self.ui.pause_pushButton.text() == "Resume":
            self.sugestions_event.clear()
            self.ui.pause_pushButton.setText("Pause")
            suggestions_thread = threading.Thread(target=self.start_suggestions_event, daemon=True)
            self.counter -= 1
            suggestions_thread.start()

    # slot/method for stop button
    def stop_suggestions(self):
        self.ui.pause_pushButton.setText("Pause")
        self.ui.start_pushButton.setText("Start")
        self.ui.pause_pushButton.setDisabled(True)
        self.counter = 0
        self.sugestions_event.set()

    # TODO: this is terrible coding my man. I wonder how many guidelines
    #  I've broken just now.
    def open_moves_selection(self):
        challenge_window.hide()
        select_window.show()


# making sure I get error messages.
_excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    _excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QtWidgets.QApplication(sys.argv)
select_window = MoveSelectWindow()
challenge_window = MoveChallengeWindow()
select_window.show()
app.exec_()
