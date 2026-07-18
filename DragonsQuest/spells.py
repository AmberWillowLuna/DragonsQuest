

class spell:
    def __init__(self, name, damage, heal, acc, desc, casting):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.acc=acc
        self.desc=desc
        self.casting=casting #chat text after casting 

    def cast(self, caster, target):
        if caster.mana >0:
            caster.mana -= 1
            target.hp -= self.damage
            caster.hp += self.heal
            print(f"{caster.name} casts {self.name} on {target.name}, dealing {self.damage} damage!")
        else:
            print(f"{caster.name} does not have enough mana to cast {self.name}.")