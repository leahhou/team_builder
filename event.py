from id_generator import IdGenerator
from algorithm import Person

event_id = IdGenerator()

class Event():
    def __init__(self, location, host, desc):
        self._id = event_id.next()
        self._location = location
        self._host = host
        self._desc = desc
        self._participants = []
        self._attendees = 0
        self._teams = []
    
    def add_participant(self, profile):
        self._participants.append(profile)
        self._attendees += 1
        profile.event.append(self._id)
    
    def remove_participant(self, id):
        for i in self._participants:
            if i.id == id:
                self._participants.remove(i)
                self._attendees -= 1
                break

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, teams):
        self._teams = teams
    
    @property
    def id(self):
        return self._id

    @property
    def participants(self):
        return self._participants