import sqlite3
import random

conn = sqlite3.connect("dz_1.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)""")
conn.commit()

a = ["hello", "world", 1, 2, 3]
print(a)

dl = 0
for i in a:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', [i])
        conn.commit()
    elif i % 2:
        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES ('нечётное')''')
        conn.commit()
k = cursor.fetchall()
print(k)

cursor.execute("SELECT COUNT (*) FROM 'tab_2'")
cursor.execute("SELECT COUNT (*) FROM 'tab_1'")
result_tab_1 = cursor.fetchall()
result_tab_2 = cursor.fetchall()
print(result_tab_1)
print(result_tab_2)
