from collections import defaultdict
from PyQt5 import QtWidgets
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

    database = os.path.abspath("./moves.db")
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


class AddDanceWindow(QtWidgets.QMainWindow):
    # init function
    def __init__(self):
        super(AddDanceWindow, self).__init__()
        self.ui = Ui_AddDanceWindow()
        self.ui.setupUi(self)
        self.assign_slots()
        self.init_db()

    # method to assign slots to buttons.
    def assign_slots(self):
        self.ui.submit_pushButton.clicked.connect(self.submit_btn_pressed)

    # method to save input data, when submit button is pressed
    def submit_btn_pressed(self):

        # TODO: make sure the name and category fields are selected.
        #       Define a class or a function to validate input, to make
        #       sure that there is input, to give visual feedback based on
        #       whether the user has valid input to submit.

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

        # adds move data to moves table
        db.add_move(self.conn, dance_move)
        self.conn.commit()

        db.print_entries(self.conn)

        time.sleep(0.5)

        # clears the input fields
        self.ui.name_lineEdit.clear()
        self.ui.category_comboBox.setCurrentIndex(0)
        self.ui.tags_lineEdit.clear()
        self.ui.description_textEdit.clear()

    # initializes dance database
    def init_db(self):
        database = os.path.abspath("./moves.db")
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


load_from_db()
app = QtWidgets.QApplication([])
application = AddDanceWindow()
application.show()
sys.exit(app.exec())
