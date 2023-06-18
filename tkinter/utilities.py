import sqlite3  as sql

class database:
    name = "yousuf.db"
    def __init__(self):
        pass

    @classmethod
    def create(cls):
        try:
            connection = sql.connect(cls.name)
            query ='''CREATE TABLE IF NOT EXISTS student (id INTEGER NOT NULL,
            rollno TEXT NOT NULL,
            gender TEXT NOT NULL,
            email TEXT ,
            phone TEXT,
            PRIAMRY KEY (id AUTOUNCREMENT));'''


            connection.execute(query)

        except sql.error as error:
            print("erreo while conecting")

        finally:
            if connection:
                connection.close()




