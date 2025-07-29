x = 50


def func(x):
    print('x дорівнює', x)
    x = 2
    print('Заміна локального x на',x)


func(x)
print('x як і раніше', x)
