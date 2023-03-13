#!/usr/bin/env python3

# python3 comes with the sqlite database built in

import sqlite3

# create a connection to the database.  If it does not exist it will be created.
conn = sqlite3.connect("mydb.db")

# the below would use a database in memory for the program
# conn = sqlite3.connect(':memory:')

# create a cursor to interact with the database
c = conn.cursor()


# create a table
# by convention, the SQL syntax should be all CAPS.  This is not strictly required though.
def create_table():
    command1 = """CREATE TABLE IF NOT EXISTS customers (
        cust_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT )"""

    c.execute(command1)


# VALID DATATYPES:
#    NULL
#    INTEGER
#    REAL
#    TEXT
#    BLOB


def data_entry():
    c.execute("INSERT INTO customers VALUES (1,'Mary','Brown','mary@gmail.com')")

    many_customers = [
        (2, "Wes", "Brown", "wes@gmail.com"),
        (3, "Steph", "Kuewa", "steph@gmail.com"),
        (4, "Dan", "Jones", "dan@optonline.net"),
    ]

    c.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers)
    conn.commit()


create_table()
data_entry()

c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchmany(3))

items = c.fetchall()

for item in items:
    print(item)

for item in items:
    print(str(item[0]) + "\t" + item[1] + "\t" + item[2] + "\t" + item[3])

c.execute("UPDATE customers SET email = 'wes2@gmail.com' WHERE cust_id = 2")
conn.commit()

c.execute("SELECT * FROM customers")
items = c.fetchall()

for item in items:
    print(str(item[0]) + "\t" + item[1] + "\t" + item[2] + "\t" + item[3])


# close connection
conn.close()
