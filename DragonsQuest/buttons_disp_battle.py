import button
import colors


def PlayerSpellsToButtons(player, scale):
    """
    Returns:
        [(spell, button), (spell, button), ...]
    """

    buttons = []

    y = 20*scale

    for spell in player.spells:

        b = button.Button(
            130*scale,
            y*scale,
            150*scale,
            30*scale,
            spell.name,
            colors.GOLD,
            (255,255,120)
        )

        buttons.append((spell, b))

        y += 12*scale

    return buttons

def PlayerItemsToButtons(player, scale):
    """
    Returns:
        [(item, button), (item, button), ...]
    """

    buttons = []

    y = 40*scale

    for item in player.inventory:

        b = button.Button(
            130*scale,
            y*scale,
            150*scale,
            30*scale,
            item.name,
            colors.GOLD,
            (255,255,120)
        )

        buttons.append((item, b))

        y += 12*scale

    return buttons