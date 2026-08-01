import basic_functions
import random

def drawRandomDragon():
    roll=random.randint(1,100)
    if roll<24:
        return BlueDragon()
    elif roll<47:
        return BlueDragon()
    elif roll<70:
        return BlueDragon()
    elif roll<92:
        return BlueDragon()
    else:
        return BlueDragon()




class dragon:
    def __init__(self, maxhp, hp, str1, dex, const, wis, char, int1, AC, gold):
        self.maxhp=maxhp
        self.hp=hp
        self.str=str1
        self.dex=dex
        self.const=const
        self.wis=wis
        self.char=char
        self.int=int1
        self.AC=AC
        self.acc=2 #bonus for accuracy (should be alwyas 0 but lets keep it)
        self.Bacc = 0 #bonus while aiming
        self.BAC = 0 #bonus while defending
        self.Bstr = 0
        self.Bdex = 0
        self.Bconst = 0
        self.Bint = 0
        self.Bwis = 0
        self.Bchar = 0
        self.dmgReduce=1 # % of dmg reduction
        
        self.ult=0
        self.gold=gold

    def WhichAttack(self, player, chat):
        roll=basic_functions.roll_dice(20)
        if roll<14:
            chat = self.Attack1(player, chat)
        elif roll<20:
            chat = self.Attack2(player, chat)
        elif self.ult==0:
            chat = self.Attack3(player, chat)
            self.ult=1
        else:
            chat = self.Attack1(player, chat)
        return chat

    def Attack1():
        return
    def Attack2():
        return
    def Attack3():
        return
    def damage(self, value, limb, chat):
        self.hp-=value*self.dmgReduce
        if(limb==self.weak_spot):
            self.hp-=4+basic_functions.roll_dice(4)
            chat+=" That was a weak spot here!"
        return chat

    def BonusLoss(self):
        if self.BAC>0:
            self.BAC -= 1
        if self.Bstr>0:
            self.Bstr -= 1
        if self.Bdex>0:
            self.Bdex -= 1
        if self.Bconst>0:
            self.Bconst -= 1
        if self.Bint>0:
            self.Bint -= 1
        if self.Bwis>0:
            self.Bwis -= 1
        if self.Bchar>0:
            self.Bchar -= 1
        if self.Bacc>0:
            self.Bacc-=1





#icey blue -fire deals bonus dmg
class BlueDragon(dragon):
    def __init__(self):
        self.type="icey blue"
        super().__init__( 120, 120,15,8,14,10,9,10,13, 200) #AC 14?
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            chat = "Blue dragon attacks with an ice spike!"
            player.damage(basic_functions.roll_dice(12))
        else:
            chat="dragon misses an ice spike shot"
        return chat

    def Attack2(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            chat = "Dragon covers you with freezing avalance"
            player.damage(basic_functions.roll_dice(8))
            if basic_functions.roll_dice(20)+player.const+player.Bconst-10<15:
                player.damage(basic_functions.roll_dice(12))
                chat += " that hurts a lot!"
            else:
                player.damage(basic_functions.roll_dice(4))
                chat += " that hurts a bit!"
        else:
            chat = "freezing avalance had not delt you any damage"
        return chat

    def Attack3(self, player, chat):
        self.dmgReduce=0.8
        chat = "dragon makes a frozen shell upon his body to protect itself! "
        return chat






#psychic grey dragon - mostly attacks wis and const saving throws 
class GreyDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="grey psychic"
        super().__init__(120, 120,12,8,13,13,13,13,13, 200) #AC 14?

#firery red dragon - weak for obanium and cristal
class RedDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="firery red"
        super().__init__(120, 120,15,8,13,10,9,10,13, 200) #AC 14?

#greenish dragon - weak for darkness and poison - very low const
class GreenDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="greenish "
        super().__init__(120, 120,15,8,5,10,9,10,16, 200) #AC 14?


#white great dragon - no weaknesses - only 8% to find - but secondary attack attacks const
#and all dmg hits a bit higher
class WhiteDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="great white"
        super().__init__(120, 120,15,8,14,10,9,10,10, 250) #AC 14?