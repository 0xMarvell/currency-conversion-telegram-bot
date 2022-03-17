import sqlite3


class DBHelper:
    def __init__(self, dbname="currency_choice.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS Choices (currency_1 text currency_2 text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_currency_1(self, choice_text):
        stmt = "INSERT INTO Choices (currency_1) VALUES (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def add_currency_2(self, choice_text):
        stmt = "INSERT INTO Choices (currency_2) VALUES (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_currency_1(self, choice_text):
        stmt = "DELETE FROM choices WHERE currency_1 = (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_currency_2(self, choice_text):
        stmt = "DELETE FROM choices WHERE currency_2 = (?)"
        args = (choice_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_choices(self):
        stmt = "SELECT description FROM choices"
        return [x[0] for x in self.conn.execute(stmt)]
