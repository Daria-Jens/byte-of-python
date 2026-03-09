class Bird:
    def __init__(self, name):
        self.name = name
        self.can_fly = True
        self.can_walk = True
        self.can_swim = False
        self.can_dive = False
    
    def __str__(self):
        """Ця функція викликається під час виведення екземпляра класу."""
        return f"i am a {self.__class__.__name__}"

tux = Bird(name="Duck")
tux.can_swim = True
