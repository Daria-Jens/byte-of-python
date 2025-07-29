def print_max(a, b):
    if a > b:
        print(a, 'є максимальним')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'є максимальним')

# пряма передача значень
print_max(3, 4)

x = 5
y = 7
# передача змінних як аргументи
print_max(x, y)
