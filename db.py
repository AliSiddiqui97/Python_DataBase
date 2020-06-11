# 5step way

# connection
# cursor
# execute
# commit
# close

# focus on , and ?
# ? local/default data
# functions usage

import sqlite3


def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT,  marks REAL)")
    conn.commit()
    conn.close()

# createtable()
def insert(roll,nam,marks):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,nam,marks) )
    conn.commit()
    conn.close()

insert(2,'haris',400)