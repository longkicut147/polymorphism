import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("C:/Users/Admin/Desktop/oop/polymorphism/")


from wild_farm.food import *

class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
    
    def make_sound(self):
        pass

    def feed(self, food:Food):
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region


