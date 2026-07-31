import basic_functions
class armor():
    def __init__(self, name, AC, desc, cost):
        self.name = name
        self.AC=AC
        self.desc=desc
        self.cost=cost
    def equip(self, player):
        player.AC += self.AC
        player.armor = self.name

    def unequip(self, player):
        player.AC -= self.AC
        player.armor = None

    def OnHitAction(self, player, attacker, damage, chat):
        pass

class basicClothes(armor):
    def __init__(self):
        super().__init__("Leather armor", 0, "Any armor is better than no armor", 0)

class leather_armor(armor):
    def __init__(self):
        super().__init__("Leather armor", 1, "Any armor is better than no armor", 16)


class rubin_amulet(armor):
    def __init__(self):
        super().__init__("Rubin amulet", 0, "may negate the dmg!", 36)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 12:
            player.hp += damage #negate dmg
            chat = (f"{player.name}'s rubin amulet glows and negates the damage from {attacker.name}'s attack!")

class steel_armor(armor):
    def __init__(self):
        super().__init__("Steel armor", 2, "A steel armor that provides good protection.", 32)

class dragon_scale_armor(armor):
    def __init__(self):
        super().__init__("Dragon scale armor", 3, "A rare armor made from dragon scales.", 64)

    def OnHitAction(self, player, attacker, damage, chat):
        attacker.hp -= basic_functions.roll_dice(4) #reflect 1 dmg to attacker

class crown_of_fools(armor):
    def __init__(self):
        super().__init__("Crown of fools", 2, "A crown that makes the wearer look foolish.", 24)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp -= basic_functions.roll_dice(4) #reflect 1 dmg to attacker
            chat = (f"{player.name}'s crown of fools glows and reflects some damage back to {player.name}!")

class chainmail(armor):
    def __init__(self):
        super().__init__("Chainmail", 1, "A chainmail armor that provides good protection.", 24)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp +=damage*0.25 #negate 25% dmg

class miths_armor(armor):
    def __init__(self):
        super().__init__("Smith's armor", 2, "A smith's armor that provides good protection.", 48)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp +=damage*0.25 #negate 25% dmg

class legendary_armor(armor):
    def __init__(self):
        super().__init__("Legendary armor", 4, "A legendary armor that provides excellent protection.", 128)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp +=damage*0.5 #negate 50% dmg
        else:
            player.hp+=damage*0.25

class grassy_armor(armor):
    def __init__(self):
        super().__init__("Grassy armor", 2, "A grassy armor that provides good protection.", 72)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp +=damage*0.4 #negate 40% dmg
        else:
            player.hp+=damage*0.1 #or 10%

class enchanted_armor(armor):
    def __init__(self):
        super().__init__("Enchanted armor", 3, "An enchanted armor that provides good protection.", 96)

    def OnHitAction(self, player, attacker, damage, chat):
        if basic_functions.roll_dice(20) > 15:
            player.hp +=damage*0.4 #negate 50% dmg
        else:
            player.hp+=damage*0.15 #or 10%

class crystal_armor(armor):
        def __init__(self):
            super().__init__("Enchanted armor", 1, "An enchanted armor that provides good protection.", 50)
        
        def OnHitAction(self, player, attacker, damage, chat):
            player.hp+=damage*0.1 