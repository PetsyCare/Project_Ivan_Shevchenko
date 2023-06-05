import sqlite3

# create DATABASE
conn = sqlite3.connect('my_db.db')

#создаем обьект-cursor
cursor = conn.cursor()

# create new table
cursor.execute('''CREATE TABLE''')


