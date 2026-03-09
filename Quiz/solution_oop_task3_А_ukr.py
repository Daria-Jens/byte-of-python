# solution oop task 3 variant A
#Задача з розділу "ООП" Завдання 3 варіант A


# parent classes
class Walker:
   def walk(self):
      return "i'm walking"
   
class Swimmer:
    def swim(self):
        return "i'm swimming"
    
class Flyer:
    def fly(self):
        return "i'm flying"
    
class Diver:
    def dive(self):
        return "i'm diving"

# child classes
class Falcon(Walker, Flyer):
    pass

class Penguin(Walker, Swimmer, Diver):
    pass

class Duck(Walker, Swimmer, Flyer, Diver):
    pass

class Eurasian_swift(Flyer):
    pass

tux = Penguin()    # створіть екземпляр класу
print(tux.dive())
