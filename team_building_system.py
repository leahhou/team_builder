from event import Event
from algorithm import Person
from profile import Login

class TeamBuildingSystem():
    def __init__(self):
        self._events = []
        self._profiles = []
        self._logins = []
    
    def add_event(self, location, host, desc):
        event = Event(location, host, desc)
        self._events.append(event)
    
    def add_login(self, login):
        self._logins.append(login)
    
    def add_profile(self, profile):
        self._profiles.append(profile)
    
    @property
    def logins(self):
        return self._logins
    
    @property
    def profiles(self):
        return self._profiles