import re
import basic_functions

def draw_random_potion():
    roll=basic_functions.roll_dice(10)
    if(roll<3):
        return small_healing_potion()
    elif roll<5:
        return medium_healing_potion()
    elif roll<6:
        return big_healing_potion()
    elif roll<7:
        return legendary_healing_potion()
    elif roll<9:
        return mana_potion()
    elif roll<10:
        return magic_potion()
    else:
        return big_healing_potion()

class item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def action():
        pass

#subclasses for different types of items
class health_potion(item):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        self.heal_amount = value

    def action(self, player):
        player.heal(self.heal_amount)
        #add gui stuff

class mana_potion(item):
    def __init__(self):
        super().__init__("mana potion", "you probably should'n drink a lot of them in a row", 1)
        self.mana_amount = 1
        self.cost=24+basic_functions.roll_dice(8)

    def action(self, player):
        player.mana += self.mana_amount
        player.mana = min(player.mana, 3)
        player.mana_exhaust-=1
        if player.mana_exhaust==0:
            player.mana_exhaust=3
            player.curse();
        #add gui stuff

class magic_potion(item):
    def __init__(self):
        super().__init__("magic potion", "it boosts all stats for a while", 0)
        self.cost=24+basic_functions.roll_dice(8)

    def action(self, player):
        player.Bstr += 5
        player.Bdex += 5
        player.Bconst += 5
        player.Bwis+=5
        player.Bint+=5
        player.Bchar+=5
        #add gui stuff


class small_healing_potion(health_potion):
    def __init__(self):
        super().__init__("tiny healing potion", "well a small bottle with some magical juice", 4)
        self.cost=20

class medium_healing_potion(health_potion):
    def __init__(self):
        super().__init__("healing potion", "love in a bottle, love in a bottle", 8)
        self.cost=40

class big_healing_potion(health_potion):
    def __init__(self):
        super().__init__("big healing potion", "thats a good healing potion", 12)
        self.cost=60

class legendary_healing_potion(health_potion):
    def __init__(self):
        super().__init__("legendary heal", "the best healing out there", 20)
        self.cost=80