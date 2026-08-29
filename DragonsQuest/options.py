import pygame
import colors
import button
import json

def options(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock):
    # Options menu
    scale = 1.0*SCREEN_WIDTH/640

    SaveAndExit = button.Button(240*scale, 220*scale, 220*scale, 40*scale, "Save and Exit", colors.NAVY_BLUE, colors.GREEN)
    back_button = button.Button(240*scale, 280*scale, 220*scale, 40*scale, "Back", colors.NAVY_BLUE, colors.GREEN)
    clock = pygame.time.Clock()
    running = True

    resolutions = ["640x360", "1280x720", "1920x1080"]
    screen_statesA = ["Windowed", "Fullscreen"]

    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

    STATE = settings["state"]
    Resolution = settings["Resolution"]


    res_button = button.Button(240*scale, 100*scale, 220*scale, 40*scale, f"Resolution: {Resolution}", colors.NAVY_BLUE, colors.GREEN)
    screen_states = button.Button(240*scale, 160*scale, 220*scale, 40*scale, f"Screen: {STATE}", colors.NAVY_BLUE, colors.GREEN)



    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check button clicks
            if back_button.is_clicked(mouse_pos, event):
                running = False
            elif res_button.is_clicked(mouse_pos, event):
                # Cycle through resolutions
                current_res_index = resolutions.index(res_button.text.split(": "))
                new_res_index = (current_res_index + 1) % len(resolutions)
                res_button.text = f"Resolution: {resolutions[new_res_index]}"
                new_width, new_height = map(int, resolutions[new_res_index].split("x"))

            elif screen_states.is_clicked(mouse_pos, event):
                # Define the list of screen states (e.g., ["Fullscreen", "Windowed"])
                screen_statesA = ["Fullscreen", "Windowed"]
                current_state_index = screen_statesA.index(screen_states.text)
                new_state_index = (current_state_index + 1) % len(screen_statesA)
                screen_states.text = screen_statesA[new_state_index]

            elif SaveAndExit.is_clicked(mouse_pos, event):
                # Save settings to file
                new_resolution = res_button.text.split(": ")
                new_state = screen_states.text  # No need to split if the text is already the state
                with open("settings.json", "w", encoding="utf-8") as file:
                    json.dump({"resolution": new_resolution, "state": new_state}, file, indent=4)
                running = False


        # Check button hover
        #back_button.check_hover(mouse_pos)

        # Draw everything
        screen.fill(colors.BLACK)
        title_text = font.render("Options", True, colors.LIGHT_BLUE)
        screen.blit(title_text, (SCREEN_WIDTH // 2, 100))

        res_button.draw(screen)
        screen_states.draw(screen)
        back_button.draw(screen)
        SaveAndExit.draw(screen)

        pygame.display.flip()
        clock.tick(60)