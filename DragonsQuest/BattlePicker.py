import pygame
import button
import colors
import ChatDisplay
import linesF



def ChooseEquipment(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player, chat):

    smallfont = pygame.font.SysFont("Arial", 18)

    # ---------- Layout ----------
    LEFT_WIDTH = SCREEN_WIDTH - 260      # reserve right panel
    RIGHT_X = LEFT_WIDTH

    panel = pygame.Rect(RIGHT_X, 0, 260, SCREEN_HEIGHT - 100)

    # Start with nothing selected
    selected_weapon = None
    selected_armor = None

    # ---------------- Buttons ----------------

    confirmButton = button.Button(
        30, 450, 220, 45,
        "Confirm",
        colors.LIGHT_BLUE,
        (100, 255, 100)
    )

    backButton = button.Button(
        280, 450, 220, 45,
        "Back",
        colors.RED,
        (255, 120, 120)
    )

    running = True

    while running:

        # recreate lists every frame so inventory updates immediately
        weapon_buttons = []
        armor_buttons = []
        item_buttons = []

        #############################
        # Weapons
        #############################

        y = 60
        for w in player.weapon:

            txt = ("● " if w == selected_weapon else "○ ") + w.name

            weapon_buttons.append((
                w,
                button.Button(
                    20,
                    y,
                    220,
                    35,
                    txt,
                    colors.LIGHT_BLUE,
                    (100,255,100)
                )
            ))

            y += 45

        #############################
        # Armors
        #############################

        y = 60

        for a in player.armor:

            txt = ("● " if a == selected_armor else "○ ") + a.name

            armor_buttons.append((
                a,
                button.Button(
                    270,
                    y,
                    220,
                    35,
                    txt,
                    colors.LIGHT_BLUE,
                    (100,255,100)
                )
            ))

            y += 45

        #############################
        # Items
        #############################

        y = 250

        for item in player.inventory:

            item_buttons.append((
                item,
                button.Button(
                    20,
                    y,
                    220,
                    35,
                    item.name,
                    colors.GOLD,
                    (255,255,120)
                )
            ))

            y += 45

        mouse = pygame.mouse.get_pos()

        for _, b in weapon_buttons:
            b.check_hover(mouse)

        for _, b in armor_buttons:
            b.check_hover(mouse)

        for _, b in item_buttons:
            b.check_hover(mouse)

        confirmButton.check_hover(mouse)
        backButton.check_hover(mouse)

        #############################
        # Events
        #############################

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            if event.type != pygame.MOUSEBUTTONDOWN:
                continue

            # Weapons
            for w, b in weapon_buttons:

                if b.is_clicked(mouse, event):
                    selected_weapon = w
                    chat = f"Selected weapon: {w.name}"

            # Armor
            for a, b in armor_buttons:

                if b.is_clicked(mouse, event):
                    selected_armor = a
                    chat = f"Selected armor: {a.name}"

            # Items
            for item, b in item_buttons:

                if b.is_clicked(mouse, event):

                    item.action(player)

                    player.inventory.remove(item)

                    chat = f"You used {item.name}"

                    break

            # Confirm
            if confirmButton.is_clicked(mouse, event):

                if selected_weapon is None:
                    chat = "Choose a weapon."
                    continue

                if selected_armor is None:
                    chat = "Choose an armor."
                    continue

                player.currentWeapon = selected_weapon
                player.currentArmor = selected_armor

                return True

            # Back
            if backButton.is_clicked(mouse, event):
                return False

        #############################
        # Draw
        #############################

        screen.fill((0,0,0))

        # Titles
        screen.blit(
            smallfont.render("Weapons", True, (255,255,255)),
            (20,20)
        )

        screen.blit(
            smallfont.render("Armor", True, (255,255,255)),
            (270,20)
        )

        screen.blit(
            smallfont.render("Items", True, (255,255,255)),
            (20,215)
        )

        # Draw buttons

        for _, b in weapon_buttons:
            b.draw(screen)

        for _, b in armor_buttons:
            b.draw(screen)

        for _, b in item_buttons:
            b.draw(screen)

        confirmButton.draw(screen)
        backButton.draw(screen)

        # Divider
        pygame.draw.line(
            screen,
            (80,80,80),
            (RIGHT_X,0),
            (RIGHT_X,SCREEN_HEIGHT-200),
            2
        )

        # Stats panel
        lines = linesF.update_lines(player, 0, None)
        linesF.draw_lines(panel, lines, smallfont, screen)

        # Chat occupies bottom-right only
        pygame.draw.rect(
            screen,
            (0,0,0),
            (RIGHT_X, SCREEN_HEIGHT-100, 260, 100)
        )

        ChatDisplay.ChatDisplay(
            chat,
            screen,
            SCREEN_WIDTH,              
            SCREEN_HEIGHT,
            smallfont
        )

        pygame.display.flip()