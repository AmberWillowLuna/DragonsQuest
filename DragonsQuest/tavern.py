

#in tavern u can buy potions, buy dragon's book where to find what are dragon's weaknesses (4 types of dragons!)
#and you get a random information each time u get in
#some info is actually usefull 
#dragon's have 2 weaknesses:
# 1 is due to its type - on the second day you have 50% chance to get the type of dragon 
# 1 is due to its body building - for example - it may take bonus dmg when hit in certain body place (hands, legs, torso, wings, head) - on day 1 and 3 u have 15% chance to find it out
#other important info are:
#discount code for smith (-10%) # 20% 1 and third day
#discount code for potions (-10%) # 20% 1 and third day
#location of treasure #15% each day - 20+roll(10) money - only second and third day
# others are useless 
#apart from that u have for each time in tavern two potions out of all types to buy

from ChatDisplay import ChatDisplay
from basic_functions import roll_dice
import button
import pygame
import items
import colors
import ChatDisplay
from linesF import update_lines, draw_lines

def ChatWithStranger(chat, player, dragon, treasure, uselessInfo, time):
    chat += " and sit next to stranger, he says: "
    roll=roll_dice(20)
    #day one
    if time.day==0:
        if roll<10:
            chat+=uselessInfo[roll]
        elif roll<13:
            chat+="The dragon was harmed, it should have weaker "+ dragon.weak_spot+". You should aim for it" #it adds flat 1+1d4 dmg
        elif roll<17:
            chat+="I know a discount here, here it is %*@&#(*#@"
            player.discountA=1
        else:
            chat+="I know a discount for smith, here it is ((&&@#&%#"
            player.discountB=1
    elif time.day==1:
        if roll<8:
            chat+=uselessInfo[roll]
        elif roll<11:
            chat+="The treasure is located in the forest. Go now and you may get it"
            treasure=1
        else:
            chat+="The dragon is definitley a "+ dragon.type+" type of dragon. You should prepare for it"
    elif time.day==2:
        if roll<7:
            chat+=uselessInfo[roll]
        elif roll<10:
            chat+="The treasure is located in the forest. Go now and you may get it"
            treasure=1
        elif roll<13:
            chat+="The dragon was harmed, it should have weaker "+ dragon.weak_spot+". You should aim for it" #it adds flat 1+1d4 dmg
        elif roll<17:
            chat+="I know a discount here, here it is %*@&#(*#@"
            player.discountA=1
        else:
            chat+="I know a discount for smith, here it is ((&&@#&%#"
            player.discountB=1

def Tavern(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, dragon):


    time.value+=1
    
    smallfont2=pygame.font.SysFont("Arial", 16)
    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = update_lines(player, time.day, time)
    chat.value = "You arrive at the tavern "

    #buttons for potions
    potions = [items.draw_random_potion(), items.draw_random_potion()]

    potion1_button=button.Button(20, 100, 440, 100, potions[0].name+" "+str(potions[0].cost), colors.NAVY_BLUE, colors.GREEN)
    potion2_button=button.Button(20, 200, 440, 100, potions[1].name+" "+str(potions[1].cost), colors.NAVY_BLUE, colors.GREEN)

    stayButton = button.Button(50, 300, 400, 100, "Stay", colors.NAVY_BLUE, colors.GREEN)
    backButton = button.Button(50, 400, 400, 100, "Back", colors.NAVY_BLUE, colors.GREEN)
  
    #20 useless facts
    uselessInfo= ["healing potions heal", "you should not drink more than 3 mana potions", "dark sword may bite u!", "dragons are dangerous",
                  "dragons are goregous", "men are so wierd", "Wienna flirts with Ken", "Arthur went abord", "king will be missing in three days",
                  "food is important for survival", "Bless you!", "arcana gets bonus dmg by ur wisdom", "There are 4 types of dragons",
                  "dragons have 2 weaknesses types", "Legends says there is a rare fifth type of dragon", "Coffe a day keeps u awake",
                  "someone flirts with someone", "You can die in this battle", "Wienna flirts with Ben", "Hello handsome"
                  ]


    treasure = 0


    ChatWithStranger(chat, player, dragon, treasure, uselessInfo, time)

    update_lines(player, time.day, time)
    running = True
    while running:
        current_time = pygame.time.get_ticks()
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if potion1_button.is_clicked(pygame.mouse.get_pos(), event):
                    if player.gold < potions[0].cost:
                        chat += "Not enough gold!"
                        continue
                    else:
                        player.gold -= potions[0].cost
                        player.inventory.append(potions[0])
                        potions[0]= items.draw_random_potion()
                        potion1_button=button.Button(20, 100, 440, 100, potions[0].name+" "+str(potions[0].cost), colors.NAVY_BLUE, colors.GREEN)


                elif potion2_button.is_clicked(pygame.mouse.get_pos(), event):
                    if player.gold < potions[1].cost:
                        chat +="Not enough gold!"
                        continue
                    else:
                        player.gold -= potions[1].cost
                        player.inventory.append(potions[1])
                        potions[1]= items.draw_random_potion()
                        potion2_button=button.Button(20, 200, 440, 100, potions[1].name+" "+str(potions[1].cost), colors.NAVY_BLUE, colors.GREEN)

                elif stayButton.is_clicked(pygame.mouse.get_pos(), event):
                    chat.value ="You stay in the tavern for a while."
                    time.add(1)

                    lines=update_lines(player, time.day, time)
                    screen.fill((0, 0, 0))
                    chat.Display()
                    draw_lines(panel, lines, smallfont2, screen)
                    pygame.display.flip()
                    pygame.time.wait(500) 
                    
                    potions = [items.draw_random_potion(), items.draw_random_potion()]
                    
                    potion1_button=button.Button(20, 100, 440, 100, potions[0].name+" "+str(potions[0].cost), colors.NAVY_BLUE, colors.GREEN)
                    potion2_button=button.Button(20, 200, 440, 100, potions[1].name+" "+str(potions[1].cost), colors.NAVY_BLUE, colors.GREEN)

                    ChatWithStranger(chat, player, dragon, treasure, uselessInfo, time)
                    if time.q == True:
                        running=False
                        treasure=0
                    # Add your stay logic here
                elif backButton.is_clicked(pygame.mouse.get_pos(), event):
                    chat.value ="You leave the tavern."
                    if treasure==1:
                        chat+=" You have found the treasure!"
                        player.gold+=20+roll_dice(10)
                        treasure=0
                    running = False
                lines=update_lines(player, time.day, time)
                    # Add your back logic here


        #drawing
        screen.fill((0, 0, 0))
        potion1_button.draw(screen)
        potion2_button.draw(screen)
        stayButton.draw(screen)
        backButton.draw(screen)
        chat.Display()
        draw_lines(panel, lines, smallfont2, screen)
        pygame.display.flip()

    return chat