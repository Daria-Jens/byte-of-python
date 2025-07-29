import sys
import time

f = None
try:
    f = open("вірш.txt")
    # наш звичайний спосіб читати файли
    while True:
        лінія = f.readline()
        if len(лінія) == 0:
            break
        print(лінія, end='')
        sys.stdout.flush()
        print("Натисніть ctrl+c зараз")
        # Щоб переконатися, що він працює деякий час
        time.sleep(2)
except IOError:
    print("Не вдалося знайти файл вірш.txt")
except Клавіатура_переривання:
    print("!! Ви скасували читання з файлу.")
finally:
    if f:
        f.close()
    print("(Очищення: файл закрито)")
