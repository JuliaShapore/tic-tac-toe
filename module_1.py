# Классы для игры "Крестики-нолики"

class Cell:
    # Список свободных клеток
    available_cells = list(range(1, 10))
    # Список победных комбинаций
    win_combinations =\
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


class Board:

    @staticmethod  # Вывод игральной доски на экран
    def print_maps():
        print(Cell.available_cells[0], end=" ")
        print(Cell.available_cells[1], end=" ")
        print(Cell.available_cells[2])

        print(Cell.available_cells[3], end=" ")
        print(Cell.available_cells[4], end=" ")
        print(Cell.available_cells[5])

        print(Cell.available_cells[6], end=" ")
        print(Cell.available_cells[7], end=" ")
        print(Cell.available_cells[8])


class Player:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod  # Делаем ход в ячейку
    def step_maps(step, symbol):
        ind = Cell.available_cells.index(step)
        Cell.available_cells[ind] = symbol

    @staticmethod  # Получаем результат игры: если комбинация совпала, то возвращаем имя победителя
    def check_win(gamer_1, gamer_2):
        win = ""

        for option in Cell.win_combinations:
            if Cell.available_cells[option[0]] == "X" and Cell.available_cells[option[1]] == "X" and Cell.available_cells[option[2]] == "X":
                win = gamer_1.name
            if Cell.available_cells[option[0]] == "O" and Cell.available_cells[option[1]] == "O" and Cell.available_cells[option[2]] == "O":
                win = gamer_2.name

        return win


class Game:

    game_over = False  # статус игры
    player1 = True  # отвечает за смену игроков
    win = ""
    max_step = 7

    @staticmethod  # Метод основной игры
    def main_game(gamer_1, gamer_2):
        while Game.game_over == False:
            # 1. Показываем карту
            Board.print_maps()
            # 2. Спросим у играющего куда делать ход
            try:  # Проверяем, ввел ли игрок цифру, если нет, то выпадает ошибка, а ввод нужно повторить заново
                if Game.player1 == True:
                    symbol = "X"
                    step = int(input("{}, ваш ход: ".format(gamer_1.name)))
                else:
                    symbol = "O"
                    step = int(input("{}, ваш ход: ".format(gamer_2.name)))
            except ValueError:
                print('Ошибка! Ваш ход может быть только числом!')
            else:
                # 3. Делаем ход в выбранную ячейку
                try:  # Проверяем, существует ли такая свободная ячейка,
                    # если нет, то выпадает ошибка, а ввод нужно повторить заново
                    Player.step_maps(step, symbol)
                    Game.max_step -= 1
                except ValueError:
                    print('Ячейка', step, 'занята или не существует! Повторите попытку!')
                else:
                    Game.win = Player.check_win(gamer_1, gamer_2)  # определим победителя
                    if Game.win != "":
                        Game.game_over = True
                    else:
                        Game.game_over = False

                    if Game.max_step == 0:
                        print('Ничья!')
                        Game.game_over = True
                        Game.win = "дружба"

                    Game.player1 = not Game.player1

        # Игра окончена. Покажем карту. Объявим победителя.
        Board.print_maps()
        print('Победил(а), {} !'.format(Game.win))