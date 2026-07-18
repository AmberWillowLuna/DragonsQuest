

class spell:
    def __init__(self, name, damage, heal, acc):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.acc=acc

    def cast(self, caster, target):
        if caster.mana >0:
            caster.mana -= 1
            target.hp -= self.damage
            caster.hp += self.heal
            print(f"{caster.name} casts {self.name} on {target.name}, dealing {self.damage} damage!")
        else:
            print(f"{caster.name} does not have enough mana to cast {self.name}.")