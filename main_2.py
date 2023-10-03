# Игра "Крестики-нолики для одного игрока и искусственного интеллекта"
import module_2 as mdl


name_1 = input('Введите имя 1-ого игрока: ')
player_1 = mdl.Player(name_1)
player_2 = mdl.Robot()

game = mdl.Game
game.main_game(player_1, player_2)

