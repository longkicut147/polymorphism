import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("C:/Users/Admin/Desktop/oop/polymorphism/")


from wild_farm.food import *
from animal import Bird


class Owl(Bird):
    scale = 0.25

    def make_sound(self):
        return "Hoot Hoot"
    
    def feed(self, food:Food):
        if type(food) == Meat:
            self.weight += food.quantity*self.scale
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}"
    
    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    scale = 0.35

    def make_sound(self):
        return "Cluck"
    
    def feed(self, food:Food):
        self.weight += food.quantity*self.scale
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"



owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)