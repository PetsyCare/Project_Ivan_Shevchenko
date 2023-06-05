#ДЗ на четверг (Ivanov_Lesson_21.py)
# 1. Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
import sqlite3
from math import floor, ceil
conn = sqlite3.connect('DB_Lesson_21.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS TBL_Lesson_21(
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            col_2 TEXT,
                                            col_3 TEXT)
                                            ''')

# Заполнить её с помощью INSERT данными (3 записи).
for i in range(3):
    cursor.execute('''INSERT INTO TBL_Lesson_21(col_2, col_3) VALUES('TEXT_COL_2', 'TEXT_COL_3')''')
conn.commit()
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
cursor.execute('''SELECT * FROM TBL_Lesson_21''')
data = cursor.fetchall()
DEL_ID = data[1][0]
cursor.execute('''DELETE FROM TBL_Lesson_21 WHERE id=?''', (DEL_ID,))
conn.commit()
UPDATE_ID = data[2][0]
cursor.execute('''UPDATE TBL_Lesson_21 SET col_2='hello world', col_3='hello world' WHERE id=?''', (UPDATE_ID,))
conn.commit()
# *Записать данные с таблицы в текстовый файл в три колонки. Первая – id, вторая и третья с данными
with open("file_lesson_21.txt", "w") as file:
    for tbl_string in data:
        file.write(str(tbl_string) + '\n')

# 2. В БД из первого задания удалить первую ПОЛОВИНУ записей, а вторую обновить на любые значения. ВРучную удалять нельзя!
# Если строк нечетное количество, то округляем в меньшую сторону!
for i in range(floor(len(data)/2)):
    DEL_ID = data[i][0]
    cursor.execute('''DELETE FROM TBL_Lesson_21 WHERE id=?''', (DEL_ID,))
conn.commit()
for i in range(ceil(len(data)/2),len(data)):
    UPDATE_ID = data[i][0]
    cursor.execute('''UPDATE TBL_Lesson_21 SET col_2='UPDATE_TEXT', col_3='UPDATE_TEXT' WHERE id=?''',(UPDATE_ID,))
conn.commit()
#3. Создать 2 таблицы в Базе Данных
cursor.execute('''CREATE TABLE IF NOT EXISTS TBL_TXT(col TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS TBL_INT(col INTEGER)''')
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
my_list = ['Home', 'Work', 29, 9, 2022]
for element in my_list:
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
    if type(element) == str:
        cursor.execute('''INSERT INTO TBL_TXT(col) VALUES(?)''', (element,))
        cursor.execute('''INSERT INTO TBL_INT(col) VALUES(?)''', (len(element),))
        conn.commit()
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во вторую таблицу слово: «нечётное»
    elif type(element) == int:
        if element % 2 == 0:
            cursor.execute('''INSERT INTO TBL_INT(col) VALUES(?)''', (element,))
        else:
            cursor.execute('''INSERT INTO TBL_TXT(col) VALUES('нечетное')''')
        conn.commit()
# Если число записей во второй таблице больше 5, то удалить первую запись в первой таблице.
# Если меньше, то обновить первую запись в первой таблице на «hello»
cursor.execute('''SELECT * FROM TBL_INT''')
data_tbl_int = cursor.fetchall()
cursor.execute('''SELECT * FROM TBL_TXT''')
data_tbl_txt = cursor.fetchall()
if len(data_tbl_int) > 5:
    cursor.execute('''DELETE FROM TBL_TXT WHERE col=?''', (data_tbl_txt[0][0]))
    conn.commit()
else:
    cursor.execute('''UPDATE TBL_TXT SET col='hello' WHERE col=?''',(data_tbl_txt[0][0],))
    conn.commit()
