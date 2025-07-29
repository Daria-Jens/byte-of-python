x = 50


def func():
    global x

    print('x дорівнює', x)
    x = 2
    print('Глобальний x змінено на', x)


func()
print('Значення x є', x)
