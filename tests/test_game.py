
from domain.board import Board
from domain.player import Player
from domain.game import Game


player = Player("Игрок", Board())
computer = Player("Компьютер", Board())

game = Game(player, computer)

print(game.current_player.name)

game.switch_turn()

print(game.current_player.name)
print(game.check_game_over())
