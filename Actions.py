from IActions import IActions
import random


class Actions(IActions):
    """A class that implements actions that a participant in a game can perform"""
    def deals_damage(self, min_range, max_range):
        damage = random.randint(min_range, max_range)
        # The damage dealt to the enemy is randomly selected in the range
        # from min_range to max_range
        return damage

    def use_first_aid_kit(self, min_low_range, max_low_range):
        additional_health = random.randint(min_low_range, max_low_range)
        # The health that a participant in the game can recover is also randomly selected
        # in the range from min_range to max_range
        return additional_health
