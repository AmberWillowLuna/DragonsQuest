from achievementManage import AchievementManage
import basic_functions
import random
import dragons
import enemies


class weapon:
    def __init__(self, name, acc, desc, cost):
        self.name = name
        self.acc=acc #bonus for accuracy
        self.desc=desc
        self.cost=cost

class basic_dagger(weapon):
    def __init__(self):
        super().__init__("Basic Dagger", 0, "A simple dagger. Not very effective.", 0)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(4)
            chat += f"{player.name} attacks {target.type} with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed {target.type} with {self.name}!"
        return chat


class iron_sword(weapon):
    def __init__(self):
        super().__init__("Iron Sword", 0, "A sturdy iron sword.", 5)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(6)
            chat += f"{player.name} attacks {target.type} with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed {target.type} with {self.name}!"
        return chat


class steel_sword(weapon):
    def __init__(self):
        super().__init__("Steel Sword", 0, "A sharp steel sword.", 10)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(8)
            chat += f"{player.name} attacks {target.type} with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed {target.type} with {self.name}!"
        return chat


class miths_hammer(weapon):
    def __init__(self):
        super().__init__("Smith's Hammer", 0, "A heavy hammer used by blacksmiths.", 15)

    def attack(self, player, target, chat):

        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(10)
            chat += f"{player.name} smashes {target.type} with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed {target.type} with {self.name}!"
        return chat


class galaxyDagger(weapon):
    def __init__(self):
        super().__init__("Galaxy Dagger", 0, "A dagger forged from the stars.", 20)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(4) + basic_functions.roll_dice(4) + 4
            chat += f"{player.name} attacks {target.type} with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed {target.type} with {self.name}!"
        return chat


class terra_blade(weapon):
    def __init__(self):
        super().__init__("Terra Blade", 1, "A blade infused with the power of the earth.", 30)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(12)
            chat += f"{player.name} strikes with {self.name}."
        else:
            dmg = basic_functions.roll_dice(4)
            chat += f"{player.name} barely clips {target.type} with {self.name}."

        target.damage(dmg, player.limb, chat, self.name)
        return chat


class enchanted_diamond_sword(weapon):
    def __init__(self):
        super().__init__("Enchanted Sword", 2, "A powerful enchanted blade.", 50)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = max(basic_functions.roll_dice(20), 5)
            chat += f"{player.name} attacks with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed!"
        return chat


class legendary_dragon_slayer(weapon):
    def __init__(self):
        super().__init__("Dragon Slayer", -2, "A legendary anti-dragon sword.", 100)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(20) + basic_functions.roll_dice(20) + basic_functions.roll_dice(10)
            chat += f"{player.name} unleashes {self.name}!"
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed!"
        return chat


class obanium_sword(weapon):
    def __init__(self):
        super().__init__("Obanium Sword", 1, "Forged from rare Obanium.", 60)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(12) + basic_functions.roll_dice(12)
            chat += f"{player.name} attacks with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed!"
        return chat


class crystal_sword(weapon):
    def __init__(self):
        super().__init__("Crystal Sword", 2, "A razor-sharp crystal blade.", 90)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(20) + basic_functions.roll_dice(12)
            chat += f"{player.name} attacks with {self.name}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed!"
        return chat


class magic_bow(weapon):
    def __init__(self):
        super().__init__("Magic Bow", 4, "A bow with magical guidance.", 40)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(12)
            chat += f"{player.name} shoots an arrow."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name}'s arrow misses!"
        return chat


class flamethrower(weapon):
    def __init__(self):
        super().__init__("Flamethrower", -1, "Sprays devastating flames.", 80)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(10) + basic_functions.roll_dice(10) + basic_functions.roll_dice(12)
            chat += f"{player.name} engulfs {target.type} in flames!"
        else:
            dmg = basic_functions.roll_dice(10)
            chat += f"{player.name}'s flames partially hit."

        target.damage(dmg, player.limb, chat, self.name)
        return chat


class mace_of_destruction(weapon):
    def __init__(self):
        super().__init__("Mace of Destruction", 1, "A weapon of overwhelming force.", 72)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(20) + basic_functions.roll_dice(20)
            chat += f"{player.name} crushes {target.type}."
            target.damage(dmg, player.limb, chat, self.name)
        else:
            chat += f"{player.name} missed!"
        return chat


class dark_sword(weapon):
    def __init__(self):
        super().__init__("Dark Sword", 2, "Powerful but cursed.", 45)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(12) + basic_functions.roll_dice(12) + basic_functions.roll_dice(12)+4
            chat += f"{player.name} channels dark power!"
            target.damage(dmg, player.limb, chat, self.name)
        else:          
            if basic_functions.roll_dice(20) > 8:
                AchievementManage.Achieve("Ouch, you traidor!")
                if player.armor!="Rubin Amulet" and player.armor!="Crown of fools":
                    selfdmg = basic_functions.roll_dice(4)-1
                    player.damage(selfdmg)
                    chat += f"The darkness backfires for {selfdmg} damage!"
                else:
                    selfdmg=basic_functions.roll_dice(2)-1
                    player.damage(selfdmg)
                    chat += f"{player.name}'s armor almost protects from the dark backlash."
        return chat


class arcanus_sword(weapon):
    def __init__(self):
        super().__init__("Arcanus Sword", 3, "An ancient arcane blade.", 150)

    def attack(self, player, target, chat):
        chat += "smash... \n"
        if basic_functions.aim(player, target, self.acc):
            dmg = basic_functions.roll_dice(20) + basic_functions.roll_dice(20) + player.wis + player.Bwis
            chat += f"{player.name} unleashes arcane energy!"
        else:
            dmg = basic_functions.roll_dice(8) + basic_functions.roll_dice(8) + 4
            chat += f"The arcane blast partially connects."

        target.damage(dmg, player.limb, chat, self.name)
        return chat