while True:
    s = input('Введіть щось :')
    if s == 'вийти':
        break
    if len(s) < 3:
        print('Занадто мало')
        continue
    print('Введений рядок достатньої довжини')
    # Різні інші дії тут...
