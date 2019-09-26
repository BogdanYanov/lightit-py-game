from Actions import Actions


class Player(Actions):
    """The base class of a player that inherits actions and has information about itself"""
    def __init__(self, name):
        """
        Variable health must contain an integer value
        The variable name must contain a string indicating the name of the player
        """
        self.__health = 100
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        # Check that when setting a new health value,
        # it does not go beyond 0 <= health <= 100
        if health < 0:
            self.__health = 0
        elif health > 100:
            self.__health = 100
        else:
            self.__health = health

    def get_name(self):
        return self.__name
