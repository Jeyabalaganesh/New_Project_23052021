class Game:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 0
        self._score = 100

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("You don't have your soul")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            del_level = level - self._level
            self._score += 5000 * del_level
            self._level = level

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name:{}, Lives:{}, Level:{}, Score:{}".format(self.name, self._lives, self._level, self._score)


jb = Game("Jb")
jb.lives -= 1
print(jb.lives)
jb.lives -= 1
print(jb.lives)
jb.lives -= 1
print(jb.lives)
jb.lives -= 1
print(jb.lives)
jb.lives -= 1
print(jb.lives)
# jb._lives -= 1
# print(jb._lives)
#
# jb.level += 3
# print(jb._score)
#
# jb.level -= 2
# print(jb._score)

print(jb.__str__())
jb.level += 3
print(jb.__str__())
jb.level -= 2
print(jb.__str__())
