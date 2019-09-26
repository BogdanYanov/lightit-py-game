import random
import CONST
import time


class Game:
    """The base class that starts the game"""
    def __init__(self):
        """
        The array players contains all the participants in the game.
        Variable current_user contains the participant in the game who makes the move
        Variable winner contains the winner of the game
        """
        self.__players = []
        self.__current_user = None
        self.__winner = None
        print("-" * 37 + "\n" + "-" * 8 + "| GAME FOR LIGHT IT |" + "-" * 8 + "\n" + "-" * 37)

    def add_players(self, *players):
        """Method of adding players"""
        for player in self.__players:
            print(player.get_name())
        for player in players:
            if player not in self.__players:
                # If a player already exists in the game,
                # you cannot add the player a second time
                self.__players.append(player)

    def select_action(self, enemy_id, action_num):
        """
        A method that calls one of three actions
        according to the action_num value and applies to an opponent
        whose ID is passed to enemy_id
        """
        enemy = self.__players[enemy_id]

        if action_num == CONST.ACTION_DAMAGE_LOW_RANGE:
            damage = self.__current_user.deals_damage(CONST.MIN_LOW_RANGE, CONST.MAX_LOW_RANGE)
            enemy.set_health(enemy.get_health() - damage)
            print(self.__current_user.get_name() + " deals " + str(damage) + " HP to " + enemy.get_name() + ". " +
                  "Now " + enemy.get_name() + " has " + str(enemy.get_health()) + " HP")

        elif action_num == CONST.ACTION_DAMAGE_HIGH_RANGE:
            damage = self.__current_user.deals_damage(CONST.MIN_HIGH_RANGE, CONST.MAX_HIGH_RANGE)
            enemy.set_health(enemy.get_health() - damage)
            print(self.__current_user.get_name() + " deals " + str(damage) + " HP to " + enemy.get_name() + ". " +
                  "Now " + enemy.get_name() + " has " + str(enemy.get_health()) + " HP")

        else:
            additional_health = self.__current_user.use_first_aid_kit(CONST.MIN_LOW_RANGE, CONST.MAX_LOW_RANGE)
            self.__current_user.set_health(self.__current_user.get_health() + additional_health)
            print(self.__current_user.get_name() + " recovery " + str(additional_health) + " HP. " +
                  "Now " + self.__current_user.get_name() + " has " + str(self.__current_user.get_health()) + " HP")

    def start(self):
        """A method that directly triggers the game"""
        if len(self.__players) < CONST.MIN_NUM_PLAYERS:
            print("Not enough players to start. Please, add at least two players")
            # Check for enough players
            return

        while True:
            # Defines the player ID who makes the move in this round
            start_player = random.randint(0, len(self.__players) - 1)

            # Set this player to current user
            self.__current_user = self.__players[start_player]

            # Defines the array ID of the remaining players, without the current user's involvement
            r = list(range(0, start_player)) + list(range(start_player + 1, len(self.__players)))

            # Defines the player ID who will be the enemy to current user
            enemy_id = random.choice(r)

            func_num = 0

            if self.__current_user.get_name == "Computer":
                func_num = random.randint(1, 6)

                if func_num > 3:
                    func_num = 3

            else:
                func_num = random.randint(1, 3)

            self.select_action(enemy_id, func_num)

            # Check the enemy health
            if self.__players[enemy_id].get_health() == 0 and len(self.__players) > CONST.MIN_NUM_PLAYERS:
                # If the enemy has no health left,
                # but the participants of the game are more than two,
                # then simply this user is removed
                print(self.__players[enemy_id].get_name() + " lost and leaves the game.")
                del self.__players[enemy_id]

            elif self.__players[enemy_id].get_health() == 0 and len(self.__players) == CONST.MIN_NUM_PLAYERS:
                # If the enemy has no health left,
                # but the participants of the game are two,
                # then we determine the winner
                print(self.__players[enemy_id].get_name() + " lost.")
                break

            time.sleep(0.5)

        self.__winner = self.__current_user

        # Print the result of game
        print(self.__winner.get_name() + " won.")
