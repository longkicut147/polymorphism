class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other:isinstance):
        return Person(str(self.name), str(other.surname))
    
    def __repr__(self):
        return self.name + " " + self.surname