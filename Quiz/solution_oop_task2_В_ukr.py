# solution oop task 2 variant B
# Задача з розділу "ООП" Завдання 2 варіант В
class Іграшка:  
    def __init__(self):
        self.ціна = 10
        self.коляр = "зелений"
    
teddy = Іграшка()
teddy.висота = 7
for ключ, значення in teddy.__dict__.items():
    print(ключ, значення)
