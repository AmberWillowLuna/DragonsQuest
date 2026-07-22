import random

def roll_dice(sides):
    return random.randint(1, sides)


def aim(player, target, bonus):
        # Calculate the hit chance based on the player's accuracy and target's evasion
    roll = roll_dice(20)+ player.acc + player.Bacc + bonus  # Player's accuracy roll

    if roll > target.AC:
        return True  # Hit
    else:
        return False  # Miss