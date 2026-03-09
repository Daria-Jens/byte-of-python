# solution chapter oop Task 5 variant A
#Задача з розділу "ООП" Завдання 4 
class Penguin(Bird):
    def __init__(self, name):
        # if using the parent class name, you must include self
        Bird.__init__(self, name)
        self.continent = "Antarctic"
        self.can_swim = True
        self.can_dive = True
        self.can_fly = False
