from id_generator import IdGenerator

team_id = IdGenerator()

class Team:
    def __init__(self, event):
        self._members = []
        self._id = team_id.next()
        self._event_id = event

    def add_member(self, person):
        self._members.append(person)
    
    @property
    def members(self):
        return self._members

    def __repr__(self):
        return str(self._members)
    
    @property
    def id(self):
        return self._id
