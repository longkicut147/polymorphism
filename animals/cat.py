from animal import Animal

class Cat(Animal):
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."

    def make_sound(self):
        return "Meow meow!"

class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.gender = "Female"

    def make_sound(self):
        return "Meow"

class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.gender = "Male"

    def make_sound(self):
        return "Hiss"