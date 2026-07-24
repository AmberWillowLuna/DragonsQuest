# make a quests class that will make GUI inside the classes 
import pygame
import button
import ChatDisplay
import basic_functions

WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
GREEN = (100, 220, 100)
RED = (220, 100, 100)


class Quest:
    def __init__(self, OptionA, OptionB, text1, text2, price):
        self.OptionA = OptionA      # "str", "dex", "time", ...
        self.OptionB = OptionB

        self.text1 = text1          # text on button A
        self.text2 = text2          # text on button B

        self.price = price
        self.finished = 0
        self.progress = 0      # how many times you've failed
        self.max_help = 5      # DC can be lowered by at most 5

        self.chat = ""

    def run(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, player, time):
        """
        Returns:
            True  -> quest completed
            False -> exited without completing
        """

        buttonA = button.Button(
            100, 180, 320, 60,
            self.text1,
            GREEN,
            (140, 255, 140)
        )

        buttonB = button.Button(
            100, 280, 320, 60,
            self.text2,
            GREEN,
            (140, 255, 140)
        )

        backButton = button.Button(
            100, 420, 320, 60,
            "Back",
            RED,
            (255, 150, 150)
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

                if backButton.is_clicked(mouse, event):
                    return False

                if buttonA.is_clicked(mouse, event):
                    if self.resolve_option(self.OptionA, player, time):
                        self.chat = f"Quest completed! You earned {self.price} gold."
                        player.gold += self.price
                        self.finished = 1
                    else:
                        self.chat = "You failed the quest."
                    return True

                if buttonB.is_clicked(mouse, event):
                    if self.resolve_option(self.OptionB, player, time):
                        self.chat = f"Quest completed! You earned {self.price} gold."
                        player.gold += self.price
                        self.finished = 1
                    else:
                        self.chat = "You failed the quest."
                    return True

            screen.fill(WHITE)

            buttonA.draw(screen)
            buttonB.draw(screen)
            backButton.draw(screen)

            ChatDisplay.ChatDisplay(
                self.chat,
                screen,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                font
            )

            pygame.display.flip()


def resolve_option(self, option, player, time):

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
        return True

    # Failed -> learn from mistakes
    self.progress += 1
    return False


import random

def RandomQuests():

    quests = [

        Quest(("str",14),("int",16),
              "Move the fallen logs",
              "Design a lever system",
              20),

        Quest(("int",14),("time",2),
              "Search the library",
              "Spend two hours searching",
              25),

        Quest(("wis",13),("time",2),
              "Search for the lost ring",
              "Search carefully for hours",
              18),

        Quest(("char",12),("wis",14),
              "Ask about the missing backpack",
              "Track the owner",
              22),

        Quest(("char",16),("str",15),
              "Calm the fighting villagers",
              "Separate them by force",
              28),

        Quest(("dex",15),("time",2),
              "Sneak into the old warehouse",
              "Wait until everyone leaves",
              30),

        Quest(("const",14),("time",1),
              "Carry supplies through the storm",
              "Take frequent rests",
              24),

        Quest(("wis",15),("int",13),
              "Investigate strange footprints",
              "Analyze the clues",
              26),

        Quest(("dex",16),("str",15),
              "Catch the runaway horse",
              "Block its path",
              30),

        Quest(("char",15),("str",14),
              "Negotiate with a merchant",
              "Blackmail merchant",
              35),

        Quest(("int",14),("dex",15),
              "Disarm an old trap",
              "Carefully dodge around it",
              28),

        Quest(("const",14),("str",14),
              "Hold a collapsing bridge",
              "Lift the support beam",
              38),

        Quest(("wis",14),("char",14),
              "Comfort a frightened child",
              "Convince them everything is safe",
              20),

        Quest(("dex",17),("time",3),
              "Steal medicine unnoticed",
              "Wait until nightfall",
              48),

        Quest(("int",15),("char",15),
              "Solve a noble's dispute",
              "Persuade both sides",
              40),

        Quest(("const",16),("wis",15),
              "Explore a poisonous cave",
              "Find a safer route",
              45)
    ]

    return random.sample(quests, 3)