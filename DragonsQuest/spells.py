
import random

def roll_dice(sides):
    return random.randint(1, sides)

class spell:
    def __init__(self, name, damage, heal, acc, desc, casting):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.acc=acc #bonus for accuracy
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

#make 7 classes of spells possible to lerarn:
#fireball, self cure, hyperfocus, turtle shells, ray of doom, poisonous breath, arcanus shot

class fireball(spell):
    def __init__(self):
        super().__init__("Fireball", random.randint(1,8)+random.randint(1,8), 0, 1, "A ball of fire that burns the enemy.", "You hurl a blazing fireball at your foe!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            if random.randint(1, 20) + self.acc >= target.ac:
                target.hp -= self.damage
                chat=(f"{player.name} casts {self.name} on {target.name}, dealing {self.damage} damage!")
            else:
                chat=(f"{player.name}'s {self.name} missed {target.name}!")
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")
