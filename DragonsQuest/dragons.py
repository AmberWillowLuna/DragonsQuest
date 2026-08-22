import basic_functions
import random
from achievementManage import AchievementManage

def drawRandomDragon():
    roll=random.randint(1,100)
    if roll<24:
        return BlueDragon()
    elif roll<47:
        return GreyDragon()
    elif roll<70:
        return RedDragon()
    elif roll<92:
        return GreenDragon()
    else:
        return drawRandomDragon()




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
            self.Attack1(player, chat)
        elif roll<20:
            self.Attack2(player, chat)
        elif self.ult==0:
            self.Attack3(player, chat)
            self.ult=1
        else:
            self.Attack1(player, chat)


    def Attack1():
        return
    def Attack2():
        return
    def Attack3():
        return
    def damage(self, value, limb, chat, weapon):
        self.hp-=value*self.dmgReduce
        if(limb==self.weak_spot):
            AchievementManage.Achieve("weak spot")
            self.hp-=4+basic_functions.roll_dice(6)
            chat+=" That was a weak spot here!"


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
        super().__init__( 160, 160,15,8,14,10,9,10,14, 200) #AC 14?
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]

    def Attack1(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            chat += "Blue dragon attacks with an ice spike!"
            player.damage(basic_functions.roll_dice(12))
        else:
            chat+="dragon misses an ice spike shot"


    def Attack2(self, player, chat):
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC:
            chat += "Dragon covers you with freezing avalance"
            player.damage(basic_functions.roll_dice(8))
            if basic_functions.roll_dice(20)+player.const+player.Bconst-10<15:
                player.damage(basic_functions.roll_dice(12))
                chat += " that hurts a lot!"
            else:
                player.damage(basic_functions.roll_dice(4))
                chat += " that hurts a bit!"
        else:
            chat += "freezing avalance had not delt you any damage"


    def Attack3(self, player, chat):
        self.dmgReduce=0.8
        chat += "dragon makes a frozen shell upon his body to protect itself! "

    def damage(self, value, limb, chat, weapon):
        self.hp-=value*self.dmgReduce
        if(limb==self.weak_spot):
            self.hp-=2+basic_functions.roll_dice(6)
            chat+=" That was a weak spot here!"
            AchievementManage.Achieve("weak spot")
        if(weapon=="flametrhower"):
            self.hp-=basic_functions.roll_dice(8)+4
            chat+=" The flamethrower is very effective against the icey dragon!"
            AchievementManage.Achieve("weakness")
        elif weapon=="enchanted diamond sword":
            self.hp-=basic_functions.roll_dice(4)+2
            chat+=" The enchanted diamond sword is effective against the icey dragon!"
            AchievementManage.Achieve("weakness")
        elif weapon == "fireball":
            self.hp -= basic_functions.roll_dice(12) + 3
            chat+=" The fireball is very effective against the icey dragon!"
            AchievementManage.Achieve("weakness")







#psychic grey dragon - mostly attacks wis and const saving throws 
class GreyDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="grey psychic"
        super().__init__(140, 140,12,8,13,13,13,13,13, 200) #AC 14?
    def Attack1(self, player, chat):
        chat+= "Grey dragon attacks with psychic blast!"
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.wis+player.Bwis-12:
            player.damage(basic_functions.roll_dice(4)+basic_functions.roll_dice(4)+basic_functions.roll_dice(4))
            chat+= " you are hit by the psychic blast"
        else:
            chat+=" you resist the psychic blast"
    def Attack2(self, player, chat):
        chat+= "Grey dragon attacks with psychic mind control!"
        x=-3
        hitpoints=0
        while basic_functions.roll_dice(20)+self.wis+self.int-20>player.wis+player.int-30+x:
            hitpoints+=max(basic_functions.roll_dice(4)+2-(player.char//5),1)
            x+=3
        chat+= f" you are hit by the psychic mind control for a while!! It dealt {hitpoints} damage"
        player.damage(hitpoints)
    def Attack3(self, player, chat):
        chat += "GREY DRAGON SEDUCES YOU!!"
        if basic_functions.roll_dice(20)+player.char+player.Bchar-10>self.char+self.Bchar+4:
            player.wis=max(player.wis-3,1)
            player.int=max(player.int-3,1)
        else:
            chat+=" you resist the seduction"

        


#firery red dragon - weak for obanium and cristal
class RedDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="firery red"
        super().__init__(125, 125,15,8,13,10,9,10,13, 200) #AC 14?
    def Attack1(self, player, chat):
        chat+= "Red dragon attacks with spikey wings!!"
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC-11:
            player.damage(basic_functions.roll_dice(4)+basic_functions.roll_dice(8))
            chat+= " you have spikes in your body..."
        else:
            chat+=" you resist the attack"
    def Attack2(self, player, chat):
        chat+= "Red dragon attacks with a fire blast"
        hitpoints=1
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC-10:
            hitpoints+=basic_functions.roll_dice(8)+basic_functions.roll_dice(8)
            chat+= f" you are hit by the blast  It dealt {hitpoints} damage"
        else:
            chat += f"you resist the fire blast, but it dealt {hitpoints} damage"
        player.damage(hitpoints)
    def Attack3(self, player, chat):
        chat += "Red dragons regain power while drinking lawa!"
        self.hp+=basic_functions.roll_dice(8)+basic_functions.roll_dice(8)+basic_functions.roll_dice(4)+4
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def damage(self, value, limb, chat, weapon):
        self.hp-=value*self.dmgReduce
        if(limb==self.weak_spot):
            self.hp-=2+basic_functions.roll_dice(6)
            chat+=" That was a weak spot here!"
            AchievementManage.Achieve("weak spot")
        if(weapon=="Obanium Sword"):
            self.hp-=basic_functions.roll_dice(6)+4
            chat+=" The Obanium is very effective against the red dragon!"
            AchievementManage.Achieve("weakness")
        elif weapon=="Crystal Sword":
            self.hp-=basic_functions.roll_dice(6)+4
            chat+=" The enchanted diamond sword is effective against the red dragon!"
            AchievementManage.Achieve("weakness")


#greenish dragon - weak for darkness and poison - very low const
class GreenDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="greenish"
        super().__init__(150, 150,15,8,5,10,9,10,16, 200) #AC 14?
    def Attack1(self, player, chat):
        chat+= "Green dragon tries to bite you!"
        if basic_functions.roll_dice(20)+self.acc+self.Bacc>player.AC+player.BAC-10:
            player.damage(basic_functions.roll_dice(10))
            chat+= " Oww... that hurts!"
        else:
            chat+=" you dodge the attack!"
    def Attack2(self, player, chat):
        chat+= "Green dragon drains your body with magic!"
        player.damage(basic_functions.roll_dice(2))
        self.hp+=basic_functions.roll_dice(2)-1
    def Attack3(self, player, chat):
        chat += "Green dragon jumps on you!"
        if basic_functions.roll_dice(20)+player.str+player.Bstr-10>self.str+self.Bstr-13:
            player.damage(max(basic_functions.roll_dice(20)+self.str-3-player.str-player.Bstr, 5))
            chat+= "It crushes you fataly!"
        else:
            chat+="You succesfuly slipped out of dragons grip!"
    def damage(self, value, limb, chat, weapon):
        self.hp-=value*self.dmgReduce
        if(limb==self.weak_spot):
            self.hp-=2+basic_functions.roll_dice(6)
            chat+=" That was a weak spot here!"
            AchievementManage.Achieve("weak spot")
        if(weapon=="Dark Sword"):
            self.hp-=basic_functions.roll_dice(12)+8
            chat+=" The Darkness is very effective against the green dragon!"
            AchievementManage.Achieve("weakness")
        elif(weapon=="Ray of Doom"):
            self.hp-=basic_functions.roll_dice(12)
            chat+=" The Ray of Doom is  effective against the green dragon!"
            AchievementManage.Achieve("weakness")

#white great dragon - no weaknesses - only 8% to find - but secondary attack attacks const
#and all dmg hits a bit higher - phisical damage has 50% reduction of dmg!
class WhiteDragon(dragon):
    def __init__(self):
        spots=["head", "arms", "legs", "torso", "wings", "tail"]
        self.weak_spot=spots[random.randint(0,len(spots)-1)]
        self.type="great white"
        super().__init__(120, 120,15,8,14,10,9,10,10, 250) #AC 14?