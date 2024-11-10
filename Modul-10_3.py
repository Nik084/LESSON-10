import threading, time, random

class Bank:

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        counter = 100
        while counter:
            time.sleep(0.2)
            add_cash = random.randint(50, 500)
            self.balance += add_cash
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {add_cash}. Баланс: {self.balance}')
            time.sleep(0.001)
            counter -= 1

    def take(self):
        counter = 100
        while counter:
            time.sleep(0.2)
            out_cash = random.randint(50, 500)
            print(f'Запрос на {out_cash}')
            if self.balance >= out_cash:
                self.balance -= out_cash
                print(f'Снятие: {out_cash}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            counter -= 1

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')