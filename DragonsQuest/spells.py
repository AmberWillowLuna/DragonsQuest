
import random
import basic_functions




class spell:
    def __init__(self, name, damage, heal, acc, desc, casting):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.acc=acc #bonus for accuracy
        self.desc=desc
        self.casting=casting #chat +text after casting 

    def cast(self, caster, target):
        if caster.mana >0:
            caster.mana -= 1
            target.hp -= self.damage
            caster.hp += self.heal

    def attack(self, bonus, target, dmg, chat, attacker):
        if random.randint(1, 20) + self.acc+ attacker.acc +attacker.Bacc >= target.AC+ target.BAC:
                hitpoints = dmg*target.dmgReduce
                chat.value=(f"{attacker.name} casts on {target.type}, dealing {hitpoints} damage!")
                target.damage(hitpoints, attacker.limb, chat, self.name)
                
        else:
            chat.value=(f"{attacker.name}'s missed {target.type}!")

#make 7 classes of spells possible to lerarn:
#fireball, self cure, hyperfocus, turtle shells, ray of doom, poisonous breath, arcanus shot


class fireball(spell):
    def __init__(self):
        super().__init__(
            "Fireball",
            random.randint(1,8)+random.randint(1,8)+random.randint(1,6),
            0,
            1,
            "A ball of fire that burns the enemy.",
            "You hurl a blazing fireball!"
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value = f"{player.name} does not have enough mana."
            return

        player.mana -= 1
        self.attack(self.acc, target, self.damage, chat, player)


class selfCure(spell):
    def __init__(self):
        super().__init__(
            "Self Cure",
            0,
            random.randint(1,4)+random.randint(1,4)+2,
            0,
            "Heals the caster.",
            "You feel rejuvenated!"
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1
        player.heal(self.heal)
        chat.value= f"{player.name} heals {self.heal} HP."


class hyperfocus(spell):
    def __init__(self):
        super().__init__(
            "Hyperfocus",
            0,
            0,
            2,
            "Increases accuracy.",
            "You focus completely."
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1
        player.Bacc += 4
        chat.value= f"{player.name} gains +4 accuracy."


class turtleShells(spell):
    def __init__(self):
        super().__init__(
            "Turtle Shells",
            0,
            0,
            0,
            "Increase armor.",
            "Your skin hardens."
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1
        player.BAC += 4
        chat.value= f"{player.name} gains +4 AC."


class rayOfDoom(spell):
    def __init__(self):
        super().__init__(
            "Ray of Doom",
            max(random.randint(1,20),5)+5,
            0,
            0,
            "A devastating ray.",
            "A ray of destruction erupts!"
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1
        self.attack(self.acc, target, self.damage, chat, player)


class poisonousBreath(spell):
    def __init__(self):
        super().__init__(
            "Poisonous Breath",
            random.randint(1,8)+2,
            0,
            0,
            "Poison attack.",
            "You breathe poisonous fumes."
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1

        dmg = 0

        save = basic_functions.roll_dice(20) + target.const + target.Bconst - 10

        if save < 15:
            dmg += self.damage

            if save < 10:
                dmg += basic_functions.roll_dice(8)+2

            if save < 5:
                dmg += basic_functions.roll_dice(8)+2

        if dmg > 0:
            chat += f"{player.name} engulfs {target.type} in poisonous gas!"
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{target.type} resists the poison."




class arcanusShot(spell):
    def __init__(self):
        super().__init__(
            "Arcanus Shot",
            random.randint(1,12),
            0,
            0,
            "An arcane projectile.",
            "A bolt of arcane energy flies forward."
        )

    def cast(self, player, target, chat):
        if player.mana <= 0:
            chat.value= f"{player.name} does not have enough mana."
            return

        player.mana -= 1

        if random.randint(1,20) + self.acc+5 >= target.AC + target.BAC:

            dmg = self.damage + max(player.wis + player.Bwis*2 - 10, 0)

            chat += f"{player.name} fires an Arcanus Shot!"
            target.damage(dmg, player.limb, chat, self.name)

        else:
            chat += f"{player.name}'s Arcanus Shot missed!"

