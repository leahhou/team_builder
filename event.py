from id_generator import IdGenerator

event_id = IdGenerator()

class Event():
    def __init__(self, location, host, desc):
        self._id = event_id.next()
        self._location = location
        self._host = host
        self._desc = desc
        self._participants = []
    
    def add_participant(self, profile):
        self._participants.append(profile)
    
    def remove_participant(self, id):
        for i in self._participants:
            if i.id == id:
                self._participants.remove(i)
                break
