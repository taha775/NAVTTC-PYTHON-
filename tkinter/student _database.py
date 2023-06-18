import sqlite3 as sql

class database:
    name = 'mam.db'

    def __init__(self):
        pass

    @classmethod
    def create(cls):
        try:
            connection = sql.connect(cls.name)
            query = '''CREATE TABLE IF NOT EXISTS student (
                         id INTEGER NOT NULL,
                         rollno TEXT NOT NULL,
                         name TEXT NOT NULL,
                         gender INTEGER NOT NULL,
                         email TEXT,
                         phone TEXT,                     
                         PRIMARY KEY(id AUTOINCREMENT)
                         );'''

            connection.execute(query)

        except sql.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_student(cls, rollno="", name="", gender=1, email="", phone=""):
        try:
            connection = sql.connect(cls.name)

            query = '''INSERT INTO student (rollno, name, gender, email, phone)
                       VALUES (?, ?, ?, ?, ?)'''

            cursor = connection.execute(query,(rollno, name, gender, email, phone))
            connection.commit()

        except sql.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if connection:
                connection.close()
