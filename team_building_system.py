from event import Event
from algorithm import Person
from profile import Login

class TeamBuildingSystem():
    def __init__(self):
        self._events = []
        self._profiles = []
        self._logins = []
        self._teams= []
    
    def add_event(self, location, host, desc):
        event = Event(location, host, desc)
        self._events.append(event)
    
    def add_login(self, login):
        self._logins.append(login)
    
    def add_profile(self, profile):
        self._profiles.append(profile)

    def add_team(self, team):
        self._teams.append(team)
    
    @property
    def logins(self):
        return self._logins
    
    @property
    def profiles(self):
        return self._profiles

    @property
    def events(self):
        return self._events
    
    @property
    def teams(self):
        return self._teams