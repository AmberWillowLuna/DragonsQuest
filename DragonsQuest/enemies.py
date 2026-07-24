import dragons
import basic_functions
#here 6 enemies for 6 fighting villagers quest!

#spider - easy medium?
class spider(dragons.dragon):
    def __init__(self):
        self.type="spider"
        super().__init__(20, 20,7,8,8,8,9,10,10)
        self.ult=1

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(6))
            chat="Spider attacks and hits you!"
        else:
            chat ="Spider attacks but misses!"
        return chat

    def Attack2(self, player):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc+4>player.AC+player.BAC:
            player.damage(basic_functions.roll_dice(6))
            chat="Spider spits poison on you!"
            if basic_functions.roll_dice(20)+player.const+player.Bconst-10<=12:
                player.damage(basic_functions.roll_dice(6))
                chat+=" Poison deals additional damage!"     
        else:
            chat ="Spider spits but misses!"
        return chat
    
#goblin - medium


#werewolf - hard


#wolf -medium


#bandit -medium


#gremlin - easy
    