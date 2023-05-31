#ДЗ на четверг (Ivanov_Lesson_19.py)
# Класс Company:
# Создайте класс Company
# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
class Company:
    levels = {
                1: 'junior',
                2: 'middle',
                3: 'senior',
                4: 'lead'
             }

# Создайте метод __init__(), внутри которого будут определены два protected свойства:
    # 1) _index - передается параметром и
    # 2) _level - принимает из словаря levels значение с ключом _index

    def __init__(self, index):
        self._index = index
        self._level = Company.levels[self._index]

# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        if self.is_lead():
            print('Вы и так уже уровня "БОГ", куда уж дальше!!!)')
        else:
            self._index += 1
            print('Поздравляем! Вы достигли уровня: ', Company.levels[self._index])


    # Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index == len(Company.levels):
            return True
        else:
            return False

# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):

# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
# 1) name - передается параметром, является публичным,
# 2)age - возраст
# 3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
        self.level = level
# Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более квалифицированным
# с помощью метода _level_up() родительского класса
    def work(self):
        self._level_up()
# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'Name: {self.name} \nAge: {self.age} \nLevel: {Company.levels[self.level]}')
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).
    @staticmethod
    def knowledge_base():
        print('******This is the programming knowledge base!******')
# Вызовите справку по программированию
Programmer.knowledge_base()
# Создайте объекты классов Company и Programmer
ItOverOne = Company(1)
Person_1 = Programmer('Shevchenko', 28, 1)
# Используя объект класса Programmer, повысьте свой уровень квалификации
Person_1.info()
Person_1.work()
Person_1.work()
Person_1.work()
Person_1.work()
# Дойдите до уровня lead