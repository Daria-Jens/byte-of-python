import sys

print('Аргументи командного рядка:')
for i in sys.argv:
    print(i)

print('\n\n Змінна  середовища PYTHONPATH містить', sys.path, '\n')
