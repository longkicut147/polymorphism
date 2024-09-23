import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("C:/Users/Admin/Desktop/oop/polymorphism/")


from wild_farm.food import *
from animal import Mammal


class Mouse(Mammal):
    scale = 0.1

    def make_sound(self):
        return "Squeak"
    
    def feed(self, food:Food):
        if type(food) == Vegetable or type(food) == Fruit:
            self.weight += food.quantity*self.scale
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}"
    
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    scale = 0.3

    def make_sound(self):
        return "Meow"
    
    def feed(self, food:Food):
        if type(food) == Vegetable or type(food) == Meat:
            self.weight += food.quantity*self.scale
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}"
    
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    scale = 0.4

    def make_sound(self):
        return "Woof"
    
    def feed(self, food:Food):
        if type(food) == Meat:
            self.weight += food.quantity*self.scale
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}"
    
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    scale = 1

    def make_sound(self):
        return "ROAR!!"
    
    def feed(self, food:Food):
        if type(food) == Meat:
            self.weight += food.quantity*self.scale
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}"
    
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"