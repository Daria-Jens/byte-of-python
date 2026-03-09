# solution oop task 1 variant B
# Задача з розділу "ООП" Завдання 1 варіант В
class Гра:
    гравець = "Bugs Bunny"
    рекорд = 1000
    кредит = 2

for ключ, значення in Гра.__dict__.items():  
    if ключ[:2] != "__":
        print(ключ, значення)
