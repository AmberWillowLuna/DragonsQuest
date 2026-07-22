
import random
import basic_functions


def attack(bonus, target, dmg, chat, attacker):
    if random.randint(1, 20) + bonus >= target.ac:
                target.hp -= dmg*target.dmgReduce
                chat=(f"{attacker.name} casts on {target.name}, dealing {dmg} damage!")
    else:
        chat=(f"{attacker.name}'s missed {target.name}!")

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
        super().__init__("Fireball", random.randint(1,8)+random.randint(1,8)+random.randint(1,6), 0, 1, "A ball of fire that burns the enemy.", "You hurl a blazing fireball at your foe!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            attack(self.acc, target, self.damage, chat)
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")

class selfCure(spell):
    def __init__(self):
        super().__init__("Self Cure", 0, random.randint(1,4)+random.randint(1,4)+2, 0, "Heals the caster.", "You feel rejuvenated as you heal yourself!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            player.hp += self.heal
            chat=(f"{player.name} casts {self.name} and heals for {self.heal} HP!")
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")


class hyperfocus(spell):
    def __init__(self):
        super().__init__("Hyperfocus", 0, 0, 2, "Increases accuracy for the next attack.", "You focus your mind and prepare for a precise strike!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            player.Bacc += 4
            chat=(f"{player.name} casts {self.name} and gains +{self.acc} accuracy for the next attack!")
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")

class turtleShells(spell):
    def __init__(self):
        super().__init__("Turtle Shells", 0, 0, 0, "Increases armor class for the next turn.", "You harden your defenses like a turtle's shell!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            player.BAC += 4
            chat=(f"{player.name} casts {self.name} and gains +{self.acc} armor class for the next turn!")
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")

class rayOfDoom(spell):
    def __init__(self):
        super().__init__("Ray of Doom", max(random.randint(1,20),5)+5, 0, 0, "A powerful ray that deals massive damage.", "You unleash a devastating ray of doom!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            attack(self.acc, target, self.damage, chat)
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")

            #rethink ray of doom and other spells

class poisonousBreath(spell):
    def __init__(self):
        super().__init__("Poisonous Breath", random.randint(1,8)+2, 0, 0, "A breath of poison that weakens the enemy.", "You exhale a cloud of poisonous gas!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            #attack(self.acc, target, self.damage, chat)
            #dmg after a consitiution save of target
            # 10 is a standard value so you should technicly add it
            saveThrow=basic_functions.roll_dice(20)+target.const+target.Bconst-10
            if saveThrow < 15:
                target.hp -= self.damage
                if saveThrow <10:
                    target.hp -= basic_functions.roll_dice(8)+2
                    if saveThrow <5:
                        target.hp -= basic_functions.roll_dice(8)+2
        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")

class arcanusShot(spell):
    def __init__(self):
        super().__init__("Arcanus Shot", random.randint(1,12), 0, 0, "A magical projectile that pierces armor.", "You conjure a bolt of arcane energy and launch it at your foe!")
    def cast(self, player, target, chat):
        if player.mana > 0:
            player.mana -= 1
            attack(self.acc, target, self.damage, chat)
            target.hp -= max(self.damage+player.wis+(player.Bwis*2)-10,0)


        else:
            chat=(f"{player.name} does not have enough mana to cast {self.name}.")