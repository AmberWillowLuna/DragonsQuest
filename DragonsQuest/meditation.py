import pygame
import random
import player
from ImageSprite import ImageSprite

def Meditate(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font):
    
    #pop up minigame for meditation - random chance to get +1 to a stat, +1 mana, +1 hp, or upper hand
    #hold q for 3 seconds to breathe in, e for 3 seconds to breathe out, then hold space for 3 seconds to focus
    #clock prepare
    text1 = font.render("Hold Q for 1 seconds to breathe in", True, (255, 255, 255))
    text2 = font.render("Hold E for 1 seconds to breathe out", True, (255, 255, 255))
     
    #make background an image
    # Initialize the sprite
    sprite = ImageSprite("assets/meditation.jpg", SCREEN_WIDTH, SCREEN_HEIGHT)


    running = True
    timer0 = pygame.time.get_ticks()
      # Key state and timer


    counter = 0

    hold_start_time = None
    required_hold_time = 500  # milliseconds

    while running:
        current_time = pygame.time.get_ticks()
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            elif event.type == pygame.KEYDOWN:
                if counter == 0 and event.key == pygame.K_q:
                    hold_start_time = current_time

                elif counter == 1 and event.key == pygame.K_e:
                    hold_start_time = current_time

            elif event.type == pygame.KEYUP:
            # Releasing the required key resets the timer
                if (
                    (counter == 0 and event.key == pygame.K_q) or
                    (counter == 1 and event.key == pygame.K_e)
                ):
                    hold_start_time = None

            # Check if the correct key is still being held
            keys = pygame.key.get_pressed()

            if counter == 0:
                if keys[pygame.K_q]:
                    if hold_start_time is not None and current_time - hold_start_time >= required_hold_time:
                        counter = 1
                        hold_start_time = None
                else:
                    hold_start_time = None

            elif counter == 1:
                if keys[pygame.K_e]:
                    if hold_start_time is not None and current_time - hold_start_time >= required_hold_time:
                        running = False
                else:
                    hold_start_time = None


        # ----- Draw -----
        screen.fill((0, 0, 0))
        sprite_group = pygame.sprite.Group()
        sprite_group.add(sprite)
        sprite_group.draw(screen)  # Draw the sprite on the screen
       
        if counter == 0:
            screen.blit(text1, (SCREEN_WIDTH // 2 - text1.get_width() // 2, 100))
        else:
            screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, 100))


        pygame.display.flip()

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

    time.add(1)
    chat = "You have meditated for a while, your mind feels refreshed"

    if z==0:
        time.add(1)
        chat = "You have meditated for way long than you wanted to, but you feel more relaxed"
        player.heal(2)
    return chat
