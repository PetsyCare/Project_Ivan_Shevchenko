#ДЗ на понедельник (Ivanov_Lesson_18.py)
# Создайте класс BankAccount, который представляет банковский счет.
class BankAccount:
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
    __account_number = None
    __balance = None
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
# Методы get_account_number и get_balance предоставляют доступ к приватным свойствам __account_number и __balance соответственно.
    def get_account_number(self):
        print('Номер счета: ', self.__account_number)

    def get_balance(self):
        print(f'Баланс: {self.__balance} USDT')
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета, при этом проверяя валидность операции (достаточно ли средств,
# корректно ли введена сумма для снятия).
    def deposit(self, deposit):
        self.__balance += deposit
        print(f'Вы успешно пополнили счет на {deposit} USDT. \nТекущий баланс: {self.__balance} USDT')
    def withdraw(self, withdraw):
        if isinstance(withdraw, int) == True and self.__balance - withdraw >= 0:
            self.__balance -= withdraw
            print(f'Вы успешно вывели {withdraw} USDT. \nТекущий баланс: {self.__balance} USDT')
        else:
            print('Ошибка операции! ')
# В основной части кода мы создаем экземпляр класса BankAccount с номером счета "123456789" и начальным балансом 1000.
Bank_Client = BankAccount(123456789, 1000)
# Затем мы используем методы для получения номера счета и баланса, а также для пополнения и снятия средств.
Bank_Client.get_account_number()
Bank_Client.get_balance()

command = ''
YorN = 'y'
while YorN != 'n':
    command = input('Пополнение( + ) / Вывод( - ) ')
    if command == '+':
        Bank_Client.deposit(int(input('Сколько USDT вы хотите внести: ')))
        YorN = input('Желаете продолжить?( Y/N )')
    elif command == '-':
        Bank_Client.withdraw(int(input('Сколько USDT вы хотите вывести: ')))
        YorN = input('Желаете продолжить?( Y/N )')
    else:
        print('Ошибка ввода!!!')
        YorN = input('Желаете продолжить?( Y/N )')
    if YorN.lower() == 'n':
        print('Сеанс завершен!')
        break
    elif YorN.lower() != 'y':
        print('Неизвестная команда!')
        YorN = input('Желаете продолжить?( Y/N )')
# Выводятся результаты операций.
