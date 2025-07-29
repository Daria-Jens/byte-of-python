try:
    text = input('Введіть щось --> ')
except EOFError:
    print('Чому ви прислалі мені символ кінця файлу?')
except KeyboardInterrupt:
    print('Ви скасували операцію.')
else:
    print('Ви увійшли{}'.format(text))
