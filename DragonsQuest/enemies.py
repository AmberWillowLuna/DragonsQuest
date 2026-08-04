import dragons
import basic_functions
#here 6 enemies for 6 fighting villagers quest!

#spider - easy medium?
class spider(dragons.dragon):
    def __init__(self):
        self.type="spider"
        spots=["head", "legs", "torso", " "]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        super().__init__(12, 12,7,8,8,8,9,10,10, 20)
        self.ult=1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(6))
            chat.value="Spider attacks and hits you!"
        else:
            chat +="Spider attacks but misses!"


    def Attack2(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc+4>player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(6))
            chat="Spider spits poison on you!"
            if basic_functions.roll_dice(20)+player.const+player.Bconst-10<=12:
                player.damage(basic_functions.roll_dice(6))
                chat+=" Poison deals additional damage!"     
        else:
            chat +="Spider spits but misses!"

    
#goblin - medium
class goblin(dragons.dragon):
    def __init__(self):
        self.type = "goblin"
        spots=["head", "arms", "legs", "torso", " "]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        super().__init__(24, 24, 9, 11, 9, 8, 8, 8, 12, 25)
        self.ult = 1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(8))
            chat += "Goblin slashes you with a rusty dagger!"
        else:
            chat += "Goblin misses!"


    def Attack2(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(4))
            chat += "Goblin tries to rob you!"

            if basic_functions.roll_dice(2) == 1:
                stolen = min(player.gold, basic_functions.roll_dice(4))
                player.gold -= stolen
                chat += f" It steals {stolen} gold!"
            else:
                chat += " But fails to steal anything."
        else:
            chat += "Goblin fumbles while trying to rob you."



#werewolf - hard
class werewolf(dragons.dragon):
    def __init__(self):
        self.type = "werewolf"
        spots=["head", "arms", "legs", "torso", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        super().__init__(40, 40, 16, 13, 15, 8, 8, 7, 14, 120)
        self.ult = 1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(12))
            chat += "Werewolf slashes you with its claws!"
        else:
            chat += "Werewolf misses!"


    def Attack2(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            save = basic_functions.roll_dice(20) + player.const + player.Bconst-10
            dmg = max(0, 20 - save)
            player.damage(dmg)
            chat += f"Werewolf bites you! The infection deals {dmg} damage."
        else:
            chat += "Werewolf lunges but misses!"



#wolf -medium
#wolf - medium
class wolf(dragons.dragon):
    def __init__(self):
        self.type = "wolf"
        spots=["head", "legs", "torso", " "]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        super().__init__(20, 20, 12, 13, 11, 8, 6, 5, 13, 40)
        self.ult = 1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(6))
            chat += "Wolf bites you!"
        else:
            chat += "Wolf misses!"


    def Attack2(self, player, chat):
        dmg = basic_functions.roll_dice(12)
        str_save=basic_functions.roll_dice(20)+player.str+player.Bstr-10
        if str_save>16:
            dmg=0
            chat += "Wolf pounces on you, but you push it away!"
        elif  str_save> 9:
            dmg //= 2
            chat += "Wolf pounces on you, but you block it partialy!"
        else:
            chat += "Wolf knocks you to the ground!"

        player.damage(dmg)
        


#bandit - hard medium
class bandit(dragons.dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", " "]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type = "bandit"
        super().__init__(24, 24, 11, 12, 11, 10, 10, 12, 13, 35)
        self.ult = 1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc > player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(8))
            chat += "Bandit stabs you!"
        else:
            chat += "Bandit misses!"


    def Attack2(self, player, chat):
        test = basic_functions.roll_dice(20) + player.int + player.Bint-10

        if test < 11:
            dmg = basic_functions.roll_dice(8)
            player.damage(dmg)
            chat += "Bandit tricks you into a vulnerable position!"
        elif test > 15:
            self.hp-=basic_functions.roll_dice(4)
            chat += "You outsmart the bandit, and it hurts itself!"
        else:
            chat += "You see through the bandit's trick."



#gremlin - easy
class gremlin(dragons.dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", " ", " "]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type = "gremlin"
        super().__init__(8, 8, 6, 14, 7, 10, 12, 10, 11, 40)
        self.ult = 1

    def Attack1(self, player, chat):
        save = basic_functions.roll_dice(20) + player.wis + player.Bwis-10

        if save < 13:
            player.damage(basic_functions.roll_dice(4))
            chat += "Gremlin unleashes vicious mockery! Its insults hurt your soul."
        else:
            chat += "You ignore the gremlin's pathetic insults."
        return chat

    def Attack2(self, player, chat):
        dodge = basic_functions.roll_dice(20) + player.dex + player.Bdex-10

        if dodge < 13:
            player.damage(basic_functions.roll_dice(4))
            chat += "Gremlin jumps onto your back and scratches you!"
        else:
            chat += "You dodge the gremlin's leap!"


import random

def drawRandomEnemy():
    roll = random.randint(1, 6)

    if roll == 1:
        return spider()
    elif roll == 2:
        return goblin()
    elif roll == 3:
        return wolf()
    elif roll == 4:
        return gremlin()
    elif roll == 5:
        return bandit()
    else:
        return werewolf()