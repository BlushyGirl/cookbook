import os
import sqlite3
from pathlib import Path
def setup_database():
    db_file='cookbook.db'
    if not os.path.exists(db_file):
        conn=sqlite3.connect(db_file)
        cursor=conn.cursor()
        cursor.execute('''CREATE TABLE cookbook(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            price REAL NOT NULL
        )''')
        books=[
            ('Кулинарная книга для чайников',2020,15.99),
             ('Рецепты итальянской кухни',2018,22.50),
             ('Выпичка и десерты от бабушки Нины',2023,25.99)
        ]
        cursor.executemany('INSERT INTO cookbook(title,year,price) VALUES(?,?,?)',books)
        conn.commit()
        conn.close()
        print('Готово!')
    else:
        print('Файл уже сущестует!')

if __name__=="__main__":
    setup_database()