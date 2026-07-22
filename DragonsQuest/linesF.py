def update_lines(player, day, time):
    k= [
        f"Player Stats:",
        f"Health: {player.hp}/{player.maxhp}",
        f"Mana: {player.mana}",
        f"Strength: {player.str + player.Bstr}",
        f"Dexterity: {player.dex + player.Bdex}",
        f"Constitution: {player.const + player.Bconst}",
        f"Wisdom: {player.wis + player.Bwis}",
        f"Intelligence: {player.int + player.Bint}",
        f"Charisma: {player.char + player.Bchar}",
        f"Day: {day}",
        f"Time: {time.value} / 16",
    ]
    for spell in player.spells:
        k.append(f"  - {spell.name}")
    return k



def draw_lines(panel, lines, smallfont, screen):
    y_offset = panel.y + 10
    for line in lines:
            line_surface = smallfont.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (panel.x + 10, y_offset))
            y_offset += line_surface.get_height()