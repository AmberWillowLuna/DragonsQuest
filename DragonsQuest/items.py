
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
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
        self.mana_amount = value

    def action(self, player):
        player.mana += self.mana_amount
        player.mana = min(player.mana, 3)
        player.mana_exhaust-=1
        if player.mana_exhaust==0:
            player.mana_exhaust=3
            player.curse();
        #add gui stuff

class magic_potion:
    def __init__(self, name, description, value):
        super().__init__(name, description, value)

    def action(self, player):
        player.Bstr += 2
        player.Bdex += 2
        player.Bconst += 2
        player.Bwis+=2
        player.Bint+=2
        player.Bchar+=2
        #add gui stuff