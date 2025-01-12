# Задача "Банковские операции"
import threading
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            inc_balance = randint(50, 500)
            self.balance += inc_balance
            print(f'Операция № {i + 1}. Пополнение: {inc_balance}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
            sleep(0.01)


    def take(self):
        for i in range(100):
            dec_balance = randint(50, 500)
            print(f'Запрос на {dec_balance}')
            if dec_balance <= self.balance:
                self.balance -= dec_balance
                print(f'Операция № {i+1}. Снятие: {dec_balance}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.01)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')




