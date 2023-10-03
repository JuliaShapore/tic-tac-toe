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


class Winner:
    @staticmethod  # Получаем результат игры: если комбинация совпала, то возвращаем имя победителя
    def check_win(gamer_1, gamer_2):
        win = ""

        for option in Cell.win_combinations:
            if Cell.available_cells[option[0]] == "X" and Cell.available_cells[option[1]] == "X" and \
                    Cell.available_cells[option[2]] == "X":
                win = gamer_1.name
            if Cell.available_cells[option[0]] == "O" and Cell.available_cells[option[1]] == "O" and \
                    Cell.available_cells[option[2]] == "O":
                win = gamer_2.name

        return win


class Player:  # Класс игрок

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod  # Делаем ход в ячейку
    def step_maps(step, symbol):
        ind = Cell.available_cells.index(step)
        Cell.available_cells[ind] = symbol


class Robot:  # Класс искусственный интеллект
    name = 'Computer'

    @staticmethod
    def check_line(sum_o, sum_x):  # Поиск линии с нужным количеством X и O на победных линиях
        step = ""
        for line in Cell.win_combinations:
            o = 0
            x = 0

            for j in range(0, 3):
                if Cell.available_cells[line[j]] == "O":
                    o += 1
                if Cell.available_cells[line[j]] == "X":
                    x += 1

            if o == sum_o and x == sum_x:
                for j in range(0, 3):
                    if Cell.available_cells[line[j]] != "O" and Cell.available_cells[line[j]] != "X":
                        step = Cell.available_cells[line[j]]

        return step

    @staticmethod
    def choose_step():
        step = ""
        # 1) если на какой-либо из победных линий 2 свои фигуры и 0 чужих - ставим
        step = Robot.check_line(2, 0)
        # 2) если на какой-либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "":
            step = Robot.check_line(0, 2)
        # 3) если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = Robot.check_line(1, 0)
        # 4) центр пуст, то занимаем центр
        if step == "":
            if Cell.available_cells[4] != "X" and Cell.available_cells[4] != "O":
                step = 5
        # 5) если центр занят, то занимаем первую ячейку
        if step == "":
            if Cell.available_cells[0] != "X" and Cell.available_cells[0] != "O":
                step = 1

        return step


class Game:

    game_over = False  # статус игры
    human = True  # отвечает за смену игроков
    win = ""

    @staticmethod  # Метод основной игры
    def main_game(person, robot):
        while Game.game_over == False:
            # 1. Показываем карту
            Board.print_maps()
            # 2. Спросим у играющего куда делать ход
            try:  # Проверяем, ввел ли игрок цифру, если нет, то выпадает ошибка, а ввод нужно повторить заново
                if Game.human == True:
                    symbol = "X"
                    step = int(input("{}, ваш ход: ".format(person.name)))
                else:  # ход за компьютером
                    print("Компьютер делает ход: ")
                    symbol = "O"
                    step = Robot.choose_step()
            except ValueError:
                print('Ошибка! Ваш ход может быть только числом!')
            else:
                # 3. Делаем ход в выбранную ячейку
                try: # Проверяем, существует ли такая свободная ячейка,
                    # если нет, то выпадает ошибка, а ввод нужно повторить заново
                    if step != "":
                        Player.step_maps(step, symbol)
                except ValueError:
                    print('Ячейка', step, 'занята или не существует! Повторите попытку!')
                else:
                    Game.win = Winner.check_win(person, robot)  # определим победителя
                    if Game.win != "":
                        Game.game_over = True
                    else:
                        Game.game_over = False

                    if step == "":
                        print("Ничья!")
                        Game.game_over = True
                        Game.win = "дружба"

                    Game.human = not Game.human

        # Игра окончена. Покажем карту. Объявим победителя.
        Board.print_maps()
        print('Победил(а), {} !'.format(Game.win))
