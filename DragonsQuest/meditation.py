import pygame
import random
import player

def Meditate(player, time, chat):
    x=random.randint(1,3)
    y=random.randint(0,5)
    z=random.randint(0,4)
    if(x==1):
        if player.maxhp<player.maxhp:
            player.heal(random.randint(1,3))
        elif player.mana<3:
            player.mana+=1
        else:
            player.uppderHand=True
    elif(x==2):
        if player.mana<3:
            player.mana+=1
        elif player.hp<player.maxhp:
             player.heal(random.randint(1,3))
        else:
            player.uppderHand=True
    else:
        if player.upperHand!=True:
            player.upperHand=True
        elif player.mana<3:
            player.mana+=1
        elif player.hp<player.maxhp:
             player.heal(random.randint(1,3))
    #handle y - +1 to random stat until 12
    if y == 0 and player.str < 12:
        player.str += 1
    elif y == 1 and player.dex < 12:
        player.dex += 1
    elif y == 2 and player.const < 12:
        player.const += 1
    elif y == 3 and player.int < 12:
        player.int += 1
    elif y == 4 and player.wis < 12:
        player.wis += 1
    elif y == 5 and player.char < 12:
        player.char += 1

    time.value+=1
    chat = "You have meditated for a while, your mind feels refreshed"

    if z==0:
        time.value+=1
        chat = "You have meditated for way long than you wanted to, but you feel more relaxed"
        player.heal(2)
