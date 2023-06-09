import sqlite3
from datetime import date


class Database:
    def __init__(self, path: str) -> None:
        self.con = sqlite3.connect(path)
        query = "CREATE TABLE IF NOT EXISTS Notes(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                "name TEXT NOT NULL, date_added DATE NOT NULL, note_text TEXT NOT NULL);"
        self.con.execute(query)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()


class Notebook:
    @staticmethod
    def add_note(name: str, note_text: str) -> None:
        current_date = date.today()

        query = 'INSERT INTO Notes (name, date_added, note_text) VALUES(?, ?, ?)'

        with Database('notebook.db') as db:
            db.con.execute(query, (name, current_date, note_text))

    @staticmethod
    def remove_note(note_name: str) -> None:
        query = "DELETE FROM Notes WHERE name = ?"

        with Database('notebook.db') as db:
            db.con.execute(query, (note_name,))

    @staticmethod
    def show_notes() -> None:
        query = 'SELECT * FROM Notes'
        with Database('notebook.db') as db:
            notes = db.con.execute(query).fetchall()
            print(notes)
