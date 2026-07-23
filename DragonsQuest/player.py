
import random
from armors import armor
import weapons
import armors

class Player:
    def __init__(self, image=None):
        #18 + rand(0-5)

        self.maxhp = 18+random.randint(0, 4)
        self.hp = self.maxhp
        self.AC = 10+random.randint(0, 2)
        self.str = 9+random.randint(0, 2)
        self.dex = 9+random.randint(0, 2)
        self.const = 9+random.randint(0, 2)
        self.int = 9+random.randint(0, 2)
        self.wis = 9+random.randint(0, 2)
        self.char = 9+random.randint(0, 2)
        self.acc=0 #bonus for accuracy (should be alwyas 0 but lets keep it)
        self.Bacc = 0 #bonus while aiming
        self.BAC = 0 #bonus while defending
        self.Bstr = 0
        self.Bdex = 0
        self.Bconst = 0
        self.Bint = 0
        self.Bwis = 0
        self.Bchar = 0
        self.dmgReduce=1 # % of dmg reduction
        self.gold=0

        self.discountA=0
        self.discountB=0

        self.spells = [];
        self.mana=3; # 3 spell sloty - ka¿dy gracz mo¿e rzuciæ 3 zaklêcia w walce
        self.mana_exhaust=3;

        self.armor = []
        self.weapon = [weapons.basic_dagger()]
        self.inventory = []
        self.upperHand= False

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

    def heal(self, val):
        self.hp+=val
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def discountPasses(self):
        self.discountA=0
        self.discountB=0

    def curse(self):
        x=random.randint(0,3);
        self.hp-=1
        if x==0:
            self.hp=self.hp-random.randint(0,4);
        elif x==1:
            self.AC-=1
        elif x==2:
            self.mana=0
        else:
            self.spells.remove(random.choice(self.spells))


            #print("You feel a dark presence around you. Your health has decreased by 1.")
            #add gui stuff
        # image filename, e.g. "10D.jpg", "JC.jpg", "Joker.jpg"
        #self.image = image or f"{sym}.jpg"
       # self.face_down = True  # hidden ("?") until the player reveals it
