import sqlite3


class DBHelper:
    def __init__(self, dbname="currency_choice.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS choices (description text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_currency_choice(self, choice_text):
        stmt = "INSERT INTO choices (description) VALUES (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_currency_choice(self, choice_text):
        stmt = "DELETE FROM choices WHERE description = (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_choices(self):
        stmt = "SELECT description FROM choices"
        return [x[0] for x in self.conn.execute(stmt)]
