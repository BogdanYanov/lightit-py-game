from Player import Player
from Game import Game

game = Game()
computer = Player("Computer")
player_name = input("Enter the name of your player: ")
player = Player(player_name)
game.add_players(computer, player)
game.start()
