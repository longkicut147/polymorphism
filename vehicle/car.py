from vehicle import Vehicle

class Car(Vehicle):
    AC_consumption = 0.9
    def drive(self, distance):
        self.fuel_quantity -= (self.fuel_consumption + self.AC_consumption)*distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    