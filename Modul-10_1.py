import threading
import time

def write_words(word_count, file_name):
    with (open(file_name, 'w', encoding='utf-8') as file):
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f' Какое-то слово № {i+1}\n')
    print(f'Завершилась запись в файл {file_name}')
    # print(threading.enumerate())
    # print(threading.current_thread())

start_1st = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f'Работа потоков 1-4: {round(time.time() - start_1st, 3)} секунды')

start_5th = time.time()
thread_5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()
print(f'Работа потоков 5-8: {round(time.time() - start_5th, 3)} секунды')
