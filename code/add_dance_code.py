from collections import defaultdict
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QColor
from code.dance_app_uis.add_dance_window import Ui_AddDanceWindow
import code.database_manager as db
import sys
import time
import os
# import json

dance_moves = dict()
tags_dict = defaultdict(set)

# TODO: Figure out how to handle tags when the app is running.
#          Likely ome pre-processing when the app first runs

# TODO: Think about input validation and stuff


# TODO: Think about how to handle loading data from data structure
#          into data structures
# this likely belongs to a different module.
def load_from_db():
    database = os.path.abspath("./moves.sqlite")
    conn = db.create_connection(database)
    # db.delete_all_moves(conn)
    if conn is None: return

    data = db.select_all_moves(conn)
    print(data)

    if not data: return

    for (name, category, tags, description) in data:
        tags = set(tags.split(';')) if tags else None
        print(len(tags) if tags else 0)
        dance_moves[name] = DanceMove(name, category, tags, description)

        if tags is None: continue

        for tag in tags:
            tags_dict[tag].add(name)

    for tag in tags_dict.keys():
        print(tag, tags_dict[tag])


class AddDanceWindow(QMainWindow):
    # init function
    def __init__(self):
        super(AddDanceWindow, self).__init__()
        self.ui = Ui_AddDanceWindow()
        self.ui.setupUi(self)
        self.assign_slots()
        self.init_db()
        # self.validator()

    # method to assign slots to buttons.
    def assign_slots(self):

        self.ui.submit_pushButton.clicked.connect(self.submit_btn_pressed)
        self.ui.clear_pushButton.clicked.connect(self.clear_fields)
        # self.ui.tags_lineEdit.textChanged.connect(lambda: self.visual_feedback(self.ui.tags_lineEdit))
        # self.ui.name_lineEdit.textChanged.connect(lambda: self.visual_feedback(self.ui.name_lineEdit))
        # self.ui.description_textEdit.textChanged.connect(lambda: self.visual_feedback(self.ui.description_textEdit))

    def validator(self):
        rx = QRegExp("\w+")
        validator = QRegExpValidator(rx)
        self.ui.name_lineEdit.setValidator(validator)
        self.ui.tags_lineEdit.setValidator(validator)

    # method to save input data, when submit button is pressed
    def submit_btn_pressed(self):

        # TODO: give visual feedback based on whether the user has valid input to submit.
        # self.validator()
        if not self.ui.name_lineEdit.text() or not self.ui.tags_lineEdit.text():
            self.show_empty_field_messagebox(self.ui.name_lineEdit.text(), self.ui.tags_lineEdit.text())
            return

        # description data is optional; sets the correct value depending on whether the user has entered a description
        description = self.ui.description_textEdit.toPlainText()
        description = description.strip() if description.strip() else None

        # convert tag input from string to list, for ease of manipulation/storage
        tags_list = [tag.strip() for tag in self.ui.tags_lineEdit.text().split(";") if tag.strip()]
        tags_list = set(tags_list) if tags_list else None

        # TODO: add a check for whether the dance move exists. Not necessary to do this check in database_manager.py

        # create a DanceMove instance
        dance_move = DanceMove(self.ui.name_lineEdit.text().strip(),
                               self.ui.category_comboBox.currentText().strip(),
                               tags_list,
                               description)

        # append the move to a dictionary
        dance_moves[dance_move.name] = dance_move

        # add move to respective tag in tags_dict
        for tag in tags_list:
            tags_dict[tag].add(dance_move.name)

        self.add_to_db(dance_move)
        time.sleep(0.5)
        self.clear_fields()

    def show_empty_field_messagebox(self, name_text, tags_text):
        empty_field_messagebox = QMessageBox()
        empty_field_messagebox.setWindowTitle("Add Dance")
        empty_field_messagebox.setIcon(QMessageBox.Warning)
        empty_field_messagebox_button = empty_field_messagebox.addButton(QMessageBox.Ok)
        empty_field_messagebox_button.setDefault(True)

        if not name_text and not tags_text:
            empty_field_messagebox.setText("Name and Tags fields are empty")
        elif not tags_text:
            empty_field_messagebox.setText("Tags field is empty")
        elif not name_text:
            empty_field_messagebox.setText("Name field is empty")

        empty_field_messagebox.exec_()

    def add_to_db(self, dance_move):

        # adds move data to moves table
        db.add_move(self.conn, dance_move)
        self.conn.commit()

        db.print_entries(self.conn)

    def clear_fields(self):
        self.ui.name_lineEdit.setText("")
        self.ui.tags_lineEdit.setText("")
        self.ui.description_textEdit.setText("")
        # self.ui.name_lineEdit.setPlaceholderText("Enter the name of the move")

    # initializes dance database
    def init_db(self):
        database = os.path.abspath("./moves.sqlite")
        sql_create_dance_table = """ CREATE TABLE IF NOT EXISTS moves (
                                           name text,
                                           category text,
                                           tags text,
                                           description text
                                       );
           """
        self.conn = db.create_connection(database)
        if self.conn is not None:
            db.create_table(self.conn, sql_create_dance_table)
        else:
            print("Error! Can't create the database connection")

    # saves dance moves to database
    # def save_to_db(self, dance_move):


class DanceMove:
    def __init__(self, name, category, tags, description):
        self.name = name
        self.category = category
        self.tags = tags
        self.description = description
        self.sessions = None


# making sure I get error messages.
_excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    _excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


load_from_db()
app = QApplication([])
add_dance_window = AddDanceWindow()
# application = AddDanceWindow()
# application.show()
# sys.exit(app.exec())
