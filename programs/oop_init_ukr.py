class Person:
    def __init__(self, ім_я):
        self.ім_я = ім_я

    def скажи_привіт(self):
        print('Привіт,моє ім_я', self.ім_я)

p = Person('Swaroop')
p.скажи_привіт()
# Попередні 2 рядки також можна записати як
# Person().скажи_привіт()
