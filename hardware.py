#!/usr/bin/python3

import sqlite3

con = sqlite3.connect('hardware.db')

cur = con.cursor()

for row in cur.execute('SELECT * FROM INTERFACES'):
    print(row)

con.close()
