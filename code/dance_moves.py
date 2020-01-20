import os
from collections import defaultdict

from code import database_manager as db


class DanceMove:
    def __init__(self, name, category, tags, description):
        self.name = name
        self.category = category
        self.tags = tags
        self.description = description
        # self.category_indexes = {"Technique/Step": 0, "Concept": 1, "Set": 2, "Choreography": 3}
        self.sessions = None


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


dance_moves = dict()
tags_dict = defaultdict(set)
