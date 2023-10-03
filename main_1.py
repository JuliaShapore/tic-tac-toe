# Игра "Крестики-нолики для двоих игроков"
import module_1 as mdl


name_1 = input('Введите имя 1-ого игрока: ')
player_1 = mdl.Player(name_1)
name_2 = input('Введите имя 2-ого игрока: ')
player_2 = mdl.Player(name_2)

game = mdl.Game
game.main_game(player_1, player_2)

