# make a quests class that will make GUI inside the classes 
from calendar import c
import pygame
from achievementManage import AchievementManage
import button
import ChatDisplay
import basic_functions
import linesF

WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
GREEN = (100, 220, 100)
RED = (220, 100, 100)


class Quest:
    def __init__(self, OptionA, OptionB, text1, text2, price, name, description):
        self.OptionA = OptionA      # "str", "dex", "time", ...
        self.OptionB = OptionB
        self.name = name
        self.text1 = text1          # text on button A
        self.text2 = text2          # text on button B
        self.description = description
        self.price = price
        self.finished = 0
        self.progress = 0      # how many times you've failed
        self.max_help = 5      # DC can be lowered by at most 5


    def run(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT,
        font, player, time, chat):
        time.add(1)
        smallfont2 = pygame.font.SysFont("Arial", 16)

        panel = pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
        lines = linesF.update_lines(player, time.day, time)

        chat += self.description
        scale = 1.0*SCREEN_WIDTH/640
        buttonA = button.Button(
            20*scale, 80*scale, 225*scale, 40*scale,
            self.text1,
            GREEN,
            (0, 255, 0)
        )

        buttonB = button.Button(
            20*scale, 140*scale, 225*scale, 40*scale,
            self.text2,
            GREEN,
            (0, 255, 0)
        )

        backButton = button.Button(
            20*scale, 200*scale, 225*scale, 40*scale,
            "Back",
            RED,
            (0, 255, 0)
        )

        running = True

        while running:

            mouse = pygame.mouse.get_pos()

            buttonA.check_hover(mouse)
            buttonB.check_hover(mouse)
            backButton.check_hover(mouse)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if buttonA.is_clicked(mouse, event):

                        if self.resolve_option(self.OptionA, player, time, chat):
                            player.gold += self.price
                            self.finished = 1
                            chat.value= f"Quest completed!\nYou received {self.price} gold."
                            lines=linesF.update_lines(player, time.day, time)
                            screen.fill((0, 0, 0))
                            chat.Display()
                            linesF.draw_lines(panel, lines, smallfont2, screen)
                            pygame.display.flip()
                            pygame.time.wait(1500)
                            running=False
                        else:
                            time.add(1)
                            chat += (
                                "You failed.\n"
                                "The task will become a little easier next time."
                            )

                    elif buttonB.is_clicked(mouse, event):

                        if self.resolve_option(self.OptionB, player, time, chat):
                            player.gold += self.price
                            self.finished = 1
                            chat.value = f"Quest completed!\nYou received {self.price} gold."
                            lines=linesF.update_lines(player, time.day, time)
                            screen.fill((0, 0, 0))
                            chat.Display()
                            linesF.draw_lines(panel, lines, smallfont2, screen)
                            pygame.display.flip()
                            pygame.time.wait(750)
                            running=False
                        else:
                            time.add(1)
                            chat += (
                                "You failed.\n"
                                "The task will become a little easier next time."
                            )

                    elif backButton.is_clicked(mouse, event):
                        return self.finished

                    lines = linesF.update_lines(player, time.day, time)

            screen.fill((0, 0, 0))

            # Title
            title = font.render(self.name, True, (255, 255, 255))
            screen.blit(title, (40, 30))

            # Reward
            reward = smallfont2.render(
                f"Reward: {self.price} gold",
                True,
                (255, 215, 0)
            )
            screen.blit(reward, (40, 70))

            buttonA.draw(screen)
            buttonB.draw(screen)
            backButton.draw(screen)

            chat.Display()

            linesF.draw_lines(
                panel,
                lines,
                smallfont2,
                screen
            )

            pygame.display.flip()

    def OneWeakness(self, chat):
        roll = basic_functions.roll_dice(100)
        if roll <16:
            chat += "You learn that the red dragon is weak to obanium and crystal."
        elif roll<31:
            chat += "You learn that the green dragon is weak to darkness and poison."
        elif roll<46:
            chat += "You learn that the icey dragon is weak to fire."
        elif roll<61:
            chat += "You learn that Grey dragon mostly attacks wisdom and const, so magic potions are useful!"

    def resolve_option(self, option, player, time, chat):

        stat = option[0]
        value = option[1]

        if stat == "time":
            time.add(value)
            return True

        # Effective DC becomes lower after failures
        dc = max(5, value - min(self.progress, self.max_help))

        if stat == "str":
            roll = basic_functions.roll_dice(20) + player.str + player.Bstr

        elif stat == "dex":
            roll = basic_functions.roll_dice(20) + player.dex + player.Bdex

        elif stat == "const":
            roll = basic_functions.roll_dice(20) + player.const + player.Bconst

        elif stat == "wis":
            roll = basic_functions.roll_dice(20) + player.wis + player.Bwis

        elif stat == "int":
            roll = basic_functions.roll_dice(20) + player.int + player.Bint

        elif stat == "char":
            roll = basic_functions.roll_dice(20) + player.char + player.Bchar
        else:
            return False
        roll-10
        if roll >= dc:
            AchievementManage.Achieve("first things first")
            AchievementManage.Quests(self.name)
            
            #learning weaknesses of the dragons!
            if self.name=="Ancient Library" and stat == "time":
                chat+="You find an ancient text which states all dragons weaknesses: icey blue - fire, red - obanium, crystal, green - darkness poison (low const), Grey - it mostly attacks wisdom and const, so magic potions are useful! "
                AchievementManage.Achieve("Thats usefull!")
                #one weakness:
            elif self.name == "Ancient Library":
                self.OneWeakness(chat)
                AchievementManage.Achieve("Intresting...")
            elif self.name == "Warehouse Job" and stat == "time":
                self.OneWeakness(chat)
                AchievementManage.Achieve("Intresting...")
            elif self.name == "Track the owner" and stat == "wis":
                self.OneWeakness(chat)
                AchievementManage.Achieve("Intresting...")
            elif self.name == "Merchant's Deal" and stat == "char":
                self.OneWeakness(chat)
                AchievementManage.Achieve("Intresting...")
            elif self.name == "Noble Dispute":
                self.OneWeakness(chat)
                AchievementManage.Achieve("Intresting...")
            elif self.name=="Medicine Heist":
                if player.hp<player.maxhp:
                    player.heal(8)
                    chat+= "you steal a bit of medicine and heal with it!"
                    AchievementManage.Achieve("Silent thief")

            return True

        # Failed -> learn from mistakes
        self.progress += 1
        if self.progress==2:
            AchievementManage.Achieve("Practice makes perfect")
        return False


import random

def RandomQuests():

    quests = [

    Quest(("str",14),("int",16),
          "Move the fallen logs",
          "Design a lever system",
          20,
          "Road Block",
          "Several large trees have fallen across the main trade road. Merchants are offering a reward to anyone who can reopen the path."),

    Quest(("int",14),("time",2),
          "Search the library", # here 100% to get one and 60% to get two types of dragons weaknesses
          "Spend two hours searching", #here 100% to get all types of dragons weaknesses and get achievement
          25,
          "Ancient Library",
          "The village librarian believes an ancient tome contains forgotten knowledge. Rumor says it may reveal information about different dragon species and their weaknesses."),

    Quest(("wis",13),("time",2),
          "Search for the lost ring",
          "Search carefully for hours",
          18,
          "Lost Ring",
          "An elderly woman has lost her wedding ring somewhere near the riverbank. She is desperate to have it returned."),

    Quest(("char",12),("wis",14),
          "Ask about the missing backpack",
          "Track the owner", #one time of dragon weakness
          22,
          "Missing Backpack",
          "A traveler misplaced an old backpack somewhere in the village. You can question the locals or search for clues yourself."),

    Quest(("char",16),("str",15),
          "Calm the fighting villagers",
          "Separate them by force",
          28,
          "Village Brawl",
          "Two villagers are about to start a serious fight in the town square. Resolve the conflict before someone gets hurt."),

    Quest(("dex",15),("time",2),
          "Sneak into the old warehouse",
          "Wait until everyone leaves", #you should learn type of dragon weakness (60%) or any other useless fact from tavern
          30,
          "Warehouse Job",
          "A suspicious warehouse may contain stolen supplies. You can sneak inside now or wait until it is empty."),

    Quest(("const",14),("time",1),
          "Carry supplies through the storm",
          "Take frequent rests",
          24,
          "Storm Delivery",
          "Essential supplies must reach a nearby farm despite terrible weather. The journey will test your endurance."),

    Quest(("wis",15),("int",13),
          "Investigate strange footprints",
          "Analyze the clues",
          26,
          "Strange Tracks",
          "Large footprints have appeared outside the village. Discover whether they belong to a dangerous beast or something harmless."),

    Quest(("dex",16),("str",15),
          "Catch the runaway horse",
          "Block its path",
          30,
          "Runaway Horse",
          "A frightened horse escaped from the stable and is running through the countryside. Bring it back before it injures itself."),

    Quest(("char",15),("str",14),
          "Negotiate with a merchant",  #you should be able to get a type of dragon weakness from negotiating with a merchant 60%?
          "Blackmail merchant",
          35,
          "Merchant's Deal",
          "A wealthy merchant refuses to honor an agreement. Convince him peacefully or force him to cooperate."),

    Quest(("int",14),("dex",15),
          "Disarm an old trap",
          "Carefully dodge around it",
          28,
          "Ancient Trap",
          "An old cellar contains a valuable chest protected by a forgotten mechanical trap. Find a safe way through."),

    Quest(("const",14),("str",14),
          "Hold a collapsing bridge",
          "Lift the support beam",
          38,
          "Broken Bridge",
          "A wooden bridge is beginning to collapse while travelers are still crossing it. Every second counts."),

    Quest(("wis",14),("char",14),
          "Comfort a frightened child",
          "Convince them everything is safe",
          20,
          "Lost Child",
          "A young child has wandered away from home and refuses to trust strangers. Help them reunite with their family."),

    Quest(("dex",17),("time",3),
          "Steal medicine unnoticed",
          "Wait until nightfall",
          48,
          "Medicine Heist",
          "A greedy noble has hoarded medicine while villagers are suffering. Recover the supplies without attracting attention."),

    Quest(("int",15),("char",15),
          "Solve a noble's dispute", #you should be able to get a type of dragon weakness from both sides (60% maybe?)
          "Persuade both sides",
          40,
          "Noble Dispute",
          "Two influential nobles are arguing over land ownership. Resolve the disagreement before it turns violent."),

    Quest(("const",16),("wis",15),
          "Explore a poisonous cave",
          "Find a safer route",
          45,
          "Poison Cave",
          "Miners discovered a cave filled with poisonous fumes. Search it for valuable minerals while avoiding the deadly gas.")
    ]

    return random.sample(quests, 3)