from id_generator import IdGenerator

team_id = IdGenerator()

class Team:
    def __init__(self):
        self._members = []
        self._id = team_id.next()

    def add_member(self, person):
        self._members.append(person)

    def __repr__(self):
        return str(self._members)
