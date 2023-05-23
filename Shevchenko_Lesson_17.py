#ДЗ на четверг (Ivanov_Lesson_17.py) - на гитхаб
# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова, то выводить все гласные, иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
#Итого - один класс, в нем только ДВА МЕТОДА
#Тест:
# object(123) --> 6
# object('abcdef') --> bcdf

class my_class:
    # класс с двумя методами
    def method_1(self,arg):
        self.arg = arg
        # ЕСЛИ АРГУМЕНТ - СТРОКА
        if isinstance(self.arg, str): # определяем принадлежность к типу str
            vowels = 'aeiouаеёиоуыэюя'
            consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъь'
            v_count = 0 # счетчик гласных букв
            c_count = 0 # счетчик согласных букв
            v_letters = ''
            c_letters = ''
            for letter in self.arg.lower():
                if letter in vowels: # если буква гласная - увеличиваем счетчик на 1
                    v_count += 1
                    v_letters += letter

                if letter in consonants: # если буква согласная - увеличиваем счетчик на 1
                    c_count += 1
                    c_letters += letter
            if v_count * c_count <= self.new_len(self.arg):
                print(v_letters)
            else:
                print(c_letters)

        # ЕСЛИ АРГУМЕНТ - ЧИСЛО
        elif isinstance(self.arg, int): # определяем принадлежность к типу int
            even_numbers = '2468'
            sum_evnumbers = 0 # счетчик четных цифр
            for number in str(self.arg):
                if number in even_numbers:
                    sum_evnumbers += int(number) # сумма четных цифр
            print(sum_evnumbers * self.new_len(self.arg))

    def new_len(self, arg):
        self.arg = arg
        count = 0
        for _ in str(self.arg):
            count += 1
        return count

object = my_class()
s = input('Введите число или текст: ')
# проверяем что ввел пользователь (число или текст)
try:
    number = int(s)
    object.method_1(number)
except ValueError:
    object.method_1(s)


