import random

# separate 'total' into 'n' random pieces (but not zero)
def subdivide(total, n):
    if total < n:
        return [total]

    sublist = []
    for i in range(1, n):
        sub = random.randint(1, total-(n-i))
        sublist.append(sub)
        total -= sub
    sublist.append(total)

    return sublist

class Player:
    def __init__(self, name, affinity):
        # player name
        self.name = name
        # player level
        self.level = 1
        # player hitpoints
        self.hp = 20
        # player weapon affinity
        self.affinity = affinity
        # player strength
        self.str = 1

        availableStats = 5
        self.atk, self.def, self.spd = subdivide(availableStats, 3)

        self.weapon = Weapon(
            name="Fist",
            atk=5,
            reqExp=1,
            abilities=
        )

    def __str__(self):
        return f'{self.name}'

class Ability:
    def __init__(self, name, critRate)

class Weapon:
    def __init__(self, name, atk, reqExp, abilities):
        self.name = name
        self.atk = atk
        self.reqExp = reqExp
        self.abilities = abilities