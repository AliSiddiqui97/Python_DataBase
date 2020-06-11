  # 5step way

# connection
# cursor
# execute
# commit
# close

# focus on , and ?
# ? local/default data
# functions usage

import psycopg2

def createtable():
    conn = psycopg2.connect("dbname= 'data2' user= 'postgres' password='postgres' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT,  marks REAL)")
    conn.commit()
    conn.close()


# createtable()

def insert(roll,nam,marks):
    conn = psycopg2.connect("dbname= 'data2' user= 'postgres' password='postgres' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll,nam,marks) )
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname= 'data2' user= 'postgres' password='postgres' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("SELECT * from data" )
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(roll):
    conn = psycopg2.connect("dbname= 'data2' user= 'postgres' password='postgres' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute( "DELETE from data where rollno =%s", (roll,))
    conn.commit()
    conn.close()
    

def update(roll,nam,marks):
    conn = psycopg2.connect("dbname= 'data2' user= 'postgres' password='postgres' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute( "UPDATE data set name =%s , marks= %s WHERE rollno =%s ", (nam, marks,roll))
    conn.commit()
    conn.close()


# insert(3,'haris',400)
# insert(4,'haris',400)
# insert(5,'haris',400)
# delete(2)
update(5,'Shahiid',20)
print(view())