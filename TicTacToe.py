import os


def my_input(prompt: str):
    _input = input(prompt)
    if _input is not (None or '') and _input.lower().replace(' ', '') == 'quit':
        quit()
    else:
        return _input


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self, _name, _identity):
        self.identity = _identity
        self.name = _name
        self.cell_pos_list = []
        self.score = 0

    def add_score(self):
        self.score += 1


class Cell:
    def __init__(self, _pos):
        self.pos = _pos  # position of cell in board
        self.state = '-'  # state of cell '-', 'X' or 'O'
        self.disp_str = f'[{self.pos}]'

    def set_state(self, _player: Player):
        if self.state == '-':
            self.state = _player.name
            self.disp_str = f' {_player.name} '
            _player.cell_pos_list.append(self.pos)


class Board:
    def __init__(self):
        # create cell list and add each cell
        self.cell_list = []
        for i in range(1, 10):
            self.cell_list.append(Cell(i))

    def print_board(self, _players: list):
        print('WELCOME TO TIC-TAC-TOE')
        print('\n' + f'Player X Score:- {_players[0].score}' + ' ' * 10 + f'Player O:- {_players[1].score}')
        # print empty line
        print()
        # print board in table form
        print('', self.cell_list[0].disp_str, ' | ', self.cell_list[1].disp_str,
              ' | ', self.cell_list[2].disp_str)
        print('', self.cell_list[3].disp_str, ' | ', self.cell_list[4].disp_str,
              ' | ', self.cell_list[5].disp_str)
        print('', self.cell_list[6].disp_str, ' | ', self.cell_list[7].disp_str,
              ' | ', self.cell_list[8].disp_str)
        print()

    def reset_board(self):
        self.cell_list = []
        for i in range(1, 10):
            self.cell_list.append(Cell(i))
        player_x.cell_pos_list = []
        player_o.cell_pos_list = []


# creates player instances
player_x = Player('X', 0)
player_o = Player('O', 1)

players = [player_x, player_o]
current_player = players[0]

# creates board
board = Board()


def get_move(_board: Board, _player: Player):
    # runs loop till get valid input
    while True:
        # getting raw input
        print(f'Enter the next move\'s position by {_player.name} according to displayed board: ')
        _input = my_input('=> ')

        if _input.lower().__contains__('quit'):
            quit()
        else:
            pass

        # converting to int
        try:
            _input = int(_input)
            # applying value range constraint
            if 1 <= _input <= 9:
                # check if pos is occupied
                if _board.cell_list[_input - 1].state != '-':
                    print('Error: Position already occupied')
                else:
                    # input valid
                    return _input
            else:
                print('Error: Enter valid position')
        except ValueError:
            # handles if unable to type-cast _input
            print('Error: Enter valid position')


def check_win(_board: Board, _player: Player):
    win_combo_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],
                      [1, 5, 9], [3, 5, 7]]

    for w_combo in win_combo_list:
        if w_combo[0] in _player.cell_pos_list and \
                w_combo[1] in _player.cell_pos_list and \
                w_combo[2] in _player.cell_pos_list:
            return True
    else:
        return False


'''
def check_tie(_board: Board):
    for i in range(len(_board.cell_list)):
        if _board.cell_list[i].state == '-':
            return False
            break
    else:
        return True
'''


def check_tie(_board: Board):
    return all(cell.state != '-' for cell in _board.cell_list)


def play_round():
    while True:
        clear_screen()

        global current_player

        board.print_board(players)

        move = get_move(board, current_player)

        board.cell_list[move - 1].set_state(current_player)

        if check_win(board, current_player):
            current_player.add_score()
            clear_screen()
            board.print_board(players)
            print()
            print(f'Player {current_player.name} has won')
            board.reset_board()
            break
        elif check_tie(board):
            clear_screen()
            board.print_board(players)
            print()
            print('Match concluded as Tie')
            board.reset_board()
            break

        current_player = players[(current_player.identity + 1) % 2]


def ask_for_next():
    while True:
        _input = my_input('\n' + "Are you ready for another Test [Y/N]:- ").lower()

        if _input in ['yes', 'y']:
            return True
        elif _input in ['no', 'n']:
            return False
        else:
            print('Error: Invalid input. Please enter "y" or "n".')


if __name__ == '__main__':
    playing = True
    while playing:
        play_round()
        playing = ask_for_next()
