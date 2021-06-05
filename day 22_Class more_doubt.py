class Game:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 0
        self._score = 100

    def _get_lives(self):
        return self._lives

    def _set_lives(self, imag):
        if imag >=0:
            self._lives = imag
        else:
            print("You dont have your soul")
            self._lives = 0

    imag = property(_get_lives, _set_lives)


jb =Game("Jb")
jb.imag -= 1
print(jb._lives)
jb.imag -= 1
print(jb._lives)
jb.imag -= 1
print(jb._lives)
jb.imag -= 1
print(jb._lives)
jb.imag -= 1
print(jb._lives)

jb._lives -= 1
print(jb._lives)