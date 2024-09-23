from vehicle import Vehicle

class Truck(Vehicle):
    AC_consumption = 1.6
    def drive(self, distance):
        if self.fuel_quantity < (self.fuel_consumption + self.AC_consumption)*distance:
            return "Cannot travel, stay home and fuel stay the same"
        else:
            self.fuel_quantity -= (self.fuel_consumption + self.AC_consumption)*distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel*95/100