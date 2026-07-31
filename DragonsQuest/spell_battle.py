import button
import colors


def PlayerSpellsToButtons(player):
    """
    Returns:
        [(spell, button), (spell, button), ...]
    """

    buttons = []

    y = 100

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