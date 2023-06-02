#ДЗ на понедельник (Ivanov_Lesson_20.py)
import sqlite3


# Вы создаете БД для учета задач в команде разработки.
conn = sqlite3.connect('TaskManager.db')

cursor = conn.cursor()
# Вам необходимо создать таблицу для хранения информации о задачах и их статусе.
# Каждая задача должна иметь уникальный идентификатор, название, описание и статус (выполнена или не выполнена).
cursor.execute(
                    '''CREATE TABLE IF NOT EXISTS tasks(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    TASK_NAME TEXT, 
                    DESCRIPTION TEXT, 
                    STATUS TEXT)'''
               )


# Напишите программу на языке Python, которая создает базу данных SQLite,
# добавляет в нее несколько задач
# и позволяет пользователю получать информацию о задачах.
exit_cmd = ''
while exit_cmd != '0':
    task_name = input('Введите название задачи: ')
    task_description = input('Описание задачи: ')
    status = input('Статус (выполнена/не выполнена): ')
    cursor.execute('''INSERT INTO tasks(TASK_NAME, DESCRIPTION, STATUS) VALUES(?,?,?)''', (task_name, task_description, status))
    conn.commit()
    exit_cmd= input('Данные внесены в таблицу tasks! \n Продолжить(Enter)/Выход(0)')


cursor.execute('''SELECT * FROM tasks''')
data = cursor.fetchall()
for task in data:
    print(*task, sep=' / ')
conn.close()