from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def refuel(self):
        pass