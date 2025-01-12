# Цель: научиться создавать классы наследованные от класса Thread.
# Задача "За честь и отвагу!"
import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        power_enemy = 100
        days = 0
        while power_enemy > 0:
            power_enemy -= self.power
            print(f'{self.name} сражается {days+1} день(дня), осталось {power_enemy} воинов')
            days += 1
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
second_knight.join()
first_knight.join()
print('Все, битвы закончились!')

#END
