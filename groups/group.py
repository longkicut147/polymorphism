class Group:
    def __init__(self, name, people:list):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(str(self.name + other.name), self.people + other.people)
    
    def __len__(self):
        return len(self.people)
    
    def __str__(self):
        return f"Group {self.name} with members {', '.join(str(i) for i in self.people)}"
    
    def __getitem__(self, index):
        return self.people[index]
    
    def __iter__(self):
        return iter(self.people)
    
    def __repr__(self):
        return repr(self.people)