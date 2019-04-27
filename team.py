from algorithm import Person

class Team():
    def __init__(self):
        self._members = []
    
    def add_member(self, person):
        self._members.append(person)