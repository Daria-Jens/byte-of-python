# "ab" є скороченням від 'a'ddress'b'ook(address book-адресна книга).

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Адрес Swaroop'а:", ab['Swaroop'])

# Видалення пари ключ-значення
del ab['Spammer']

print('\nВ адресній книзі {} контакта\n'.format(len(ab)))

for ім_я, адреса in ab.items():
    print('Контакт {} за адресою: {}'.format(ім_я, адреса))

# Додавання пари ключ-значення
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

