import basic_functions
import random



class weapon:
    def __init__(self, name, acc, desc, cost):
        self.name = name
        self.acc=acc #bonus for accuracy
        self.desc=desc
        self.cost

class basic_dagger(weapon):
    def __init__(self):
        super().__init__("Basic Dagger", 0, "A simple dagger. Not very effective.",0)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(4)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

#making all weapons as classes 
class iron_sword(weapon):
    def __init__(self):
        super().__init__("Iron Sword", 0,"A sturdy iron sword.", 5)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(6)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")


class steel_sword(weapon):
    def __init__(self):
        super().__init__("Steel Sword", 0,"A sharp steel sword.", 10)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(8)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class miths_hammer(weapon):
    def __init__(self):
        super().__init__("Smith's Hammer", 0, "A heavy hammer used by blacksmiths.", 15)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(10)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class galaxyDagger(weapon):
    def __init__(self):
        super().__init__("Galaxy Dagger", 0, "A dagger forged from the stars.", 20)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(4)+basic_functions.roll_dice(4)+4
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class terra_blade(weapon):
    def __init__(self):
        super().__init__("Terra Blade", 1, "A blade infused with the power of the earth, hits even if misses.", 30)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(12)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            target.hp -= basic_functions.roll_dice(4)
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class enchanted_diamond_sword(weapon):
    def __init__(self):
        super().__init__("Enchanted Diamond Sword", 2, "A sword made of enchanted diamond, very powerful.", 50)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= max(basic_functions.roll_dice(20),5)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class legendary_dragon_slayer(weapon):
    def __init__(self):
        super().__init__("Legendary Dragon Slayer", -2, "A legendary sword capable of slaying dragons, but hard to aim with it", 100)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(20)+basic_functions.roll_dice(20)+basic_functions.roll_dice(10)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class obanium_sword(weapon):
    def __init__(self):
        super().__init__("Obanium Sword", 1, "A sword made of Obanium, a rare and powerful material.", 60)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(12)+basic_functions.roll_dice(12)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class crystal_sword(weapon):
    def __init__(self):
        super().__init__("Crystal Sword", 2, "A sword made of crystal, very sharp and accurate.", 90)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(20)+basic_functions.roll_dice(12)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class magic_bow(weapon):
    def __init__(self):
        super().__init__("Crystal Sword", 4, "A bow with a bit of autoaim", 40)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(12)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class flamethrower(weapon):
    def __init__(self):
        super().__init__("Flamethrower", -1, "A flamethrower that deals fire damage.", 80)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(10)+basic_functions.roll_dice(10)+basic_functions.roll_dice(10)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            target.hp -= basic_functions.roll_dice(10)
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class mace_of_destruction(weapon):
    def __init__(self):
        super().__init__("Mace of Destruction", 0, "A mace that deals massive damage.", 72)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(20)+basic_functions.roll_dice(20)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class dark_sword(weapon):
    def __init__(self):
        super().__init__("Dark Sword", 0, "A sword that deals dark damage, can hit the user sometimes!", 45)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(12)+basic_functions.roll_dice(12)+basic_functions.roll_dice(12)
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            player.hp -= basic_functions.roll_dice(6)
            chat=(f"{player.name} missed {target.name} with {self.name}!")

class arcanus_sword(weapon):
    def __init__(self):
        super().__init__("Arcanus Sword", 3, "A sword that deals arcane damage, very powerful and accurate.", 150)

    def attack(self, player, target, chat, cost):
        if basic_functions.aim(player, target, self.acc):
            target.hp -= basic_functions.roll_dice(20)+basic_functions.roll_dice(20)+player.wis+player.Bwis+10
            chat=(f"{player.name} attacks {target.name} with {self.name}")
        else:
            target.hp-= basic_functions.roll_dice(8)+basic_functions.roll_dice(8)+4
            chat=(f"{player.name} missed {target.name} with {self.name}!")