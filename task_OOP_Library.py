# Представьте, что вы создаете программу для управления библиотекой книг.
# Вам нужно реализовать классы для книги (Book) и библиотеки (Library). Вот требования к классам:
# Класс Book:
# Имеет атрибуты: название (title), автор (author), год выпуска (year) и статус (status).
class Book:
    def __init__(self, title: str, author: str, year: int, status: str ):
        self.title = title
        self.author = author
        self.year = year
        self.status = status


# Статус книги может быть "в наличии" или "выдана".
# Имеет методы: изменить статус книги на "выдана" (set_issued),
    # изменить статус книги на "в наличии" (set_available),
    # получить текущий статус (get_status).
    def set_issued(self):
        self.status = 'выдана'
    def set_available(self):
        self.status = 'в наличии'
    def get_status(self):
        return self.status
# Класс Library:
# Имеет атрибуты: список книг (books).
class Library():
    def __int__(self, books):
        self.books = books

# Имеет методы: добавить книгу в библиотеку (add_book), удалить книгу из библиотеки (remove_book), найти книгу по названию (find_book_by_title), найти книги по автору (find_books_by_author).
# Твоя задача:
# Создай классы Book и Library с соответствующими атрибутами и методами.
# Создай объект класса Library.
# Добавь несколько книг в библиотеку.
# Проверь функциональность методов класса Library, найдя книги по названию и автору, а также изменив статус некоторых книг.
# Удачи с задачей по ООП в Python! Если у тебя возникнут вопросы, не стесняйся задавать.