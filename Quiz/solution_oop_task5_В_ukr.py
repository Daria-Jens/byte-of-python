# solution chapter oop Task 5 variant B
# розв’язання з розділу "ООП" Завдання 5 варіант В 
class Penguin(Bird):
    def __init__(self, name):
        # використовуючи super() для звернення до батьківського класу
        super().__init__(name) # self не потрібен
        self.continent = "Antarctic"
        self.can_swim = True
        self.can_dive = True
        self.can_fly = False
