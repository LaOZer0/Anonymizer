import sqlite3


con = sqlite3.connect("fake.db")
cur = con.cursor()


def init_db():
    with open('db/create_fake_db.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    cur.executescript(sql_script)
    con.commit()
