from id_generator import IdGenerator

profile_id = IdGenerator()

class Profile():
    def __init__(self, name, langs, pos, exp, idea):
        self._name = name
        self._langs = langs
        self._pos = pos
        self._exp = exp
        self._idea = idea
        self._id = profile_id.next()
    
    @property
    def id(self):
        return self._id