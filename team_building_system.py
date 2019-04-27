from event import Event
from profile import Person

class TeamBuildingSystem():
    def __init__(self):
        self._events = []
        self._profiles = []
        self._logins = []
    
    def add_event(self, location, host, desc):
        event = Event(location, host, desc)
        self._events.append(event)
    
    def add_member(self, person):
        self._members.append(person)
    
    @property
    def logins(self):
        return logins