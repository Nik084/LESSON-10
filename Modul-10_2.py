import threading
import time

lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self, name):
        counter = 100
        delay = 1
        days = delay
        while counter:
            time.sleep(delay)
            print(f'{name} сражается {days} день(дня)..., осталось {counter - self.power} воинов')
            days += 1
            counter -= self.power
        print(f'{self.name} одержал победу спустя {days - 1} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        with lock:
            self.timer(self.name)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
