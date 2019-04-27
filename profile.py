from id_generator import IdGenerator

profile_id = IdGenerator()

class Login():
    def __init__(self, username, password, user_type):
        self._username = username
        self._password = password
        self._user_type = user_type
        self._id = profile_id.next()
    
    @property
    def id(self):
        return self._id
    
    def verify(self, username, password):
        if username == self._username and password == self._password:
            return True
        return False
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password