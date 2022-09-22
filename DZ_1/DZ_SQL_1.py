import sqlite3

# Создаём Базу данных
conn = sqlite3.connect('name1.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
title VARCHAR(50),
author VARCHAR(30),
price DECIMAL(8, 2),
amount INT) ''')

# Заполняем таблицу данными
cursor.execute('''INSERT INTO book(title,author, price, amount) VALUES ('Skazka','Pushkin', 3.5, 7)''')
# Сохраняем изменения
conn.commit()

cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
print(k)