import button
import colors


def PlayerSpellsToButtons(player):
    """
    Returns:
        [(spell, button), (spell, button), ...]
    """

    buttons = []

    y = 120

    for spell in player.spells:

        b = button.Button(
            270,
            y,
            260,
            45,
            spell.name,
            colors.GOLD,
            (255,255,120)
        )

        buttons.append((spell, b))

        y += 55

    return buttons

def PlayerItemsToButtons(player):
    """
    Returns:
        [(item, button), (item, button), ...]
    """

    buttons = []

    y = 120

    for item in player.inventory:

        b = button.Button(
            270,
            y,
            260,
            45,
            item.name,
            colors.GOLD,
            (255,255,120)
        )

        buttons.append((item, b))

        y += 55

    return buttons