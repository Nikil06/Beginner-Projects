# -------------------------------------------------------------------------------------
# Defined Constants
WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]

COLOUR_THEME = {
    'PLAYER X'    : '\033[1;34m',  # BOLD BLUE
    'PLAYER O'    : '\033[1;31m',  # BOLD RED
    'CELL DEFAULT': '\033[1;37m',  # BOLD WHITE
    'BOARD'       : '\033[1;32m',  # BOLD GREEN
    'GET INPUT'   : '\033[1;36m',  # BOLD CYAN
    'ERROR'       : '\033[1;91m',  # HI BOLD RED
    'RESET'       : '\033[0m',     # RESET TO DEFAULT PRINT
    'WIN'         : '\033[7m',  # NEGATIVE
    'TIE'         : '\033[7m'   # NEGATIVE
}
# -------------------------------------------------------------------------------------
# Player Structure
player_x = {'name': 'X', 'marked cells': [], 'score': 0, 'colour': COLOUR_THEME['PLAYER X']}

player_o = {'name': 'O', 'marked cells': [], 'score': 0, 'colour': COLOUR_THEME['PLAYER O']}

current_player = player_o


def add_score(player):
    player['score'] += 1


def switch_players():
    global current_player, player_x, player_o
    if current_player == player_x:
        current_player = player_o
    elif current_player == player_o:
        current_player = player_x


def end_program():
    print('\n'*2+'Credits: Nikil O Sivakumaar')
    quit()
# -------------------------------------------------------------------------------------
# Cell Structure
def create_cell(pos):
    return {
        'pos': pos,
        'state': '-',
        'display str': COLOUR_THEME['CELL DEFAULT'] + '[{}]'.format(pos) + COLOUR_THEME['BOARD']
    }
# -------------------------------------------------------------------------------------
# Board Structure
def create_board():
    _board = {}
    for pos in range(1, 10):
        _board[pos] = create_cell(pos)
    return _board


board = create_board()


def print_board():
    print(COLOUR_THEME['BOARD'])
    print(' ============================= ')
    print('|         TIC-TAC-TOE         |')
    print(' ============================= ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[1]['display str'], board[2]['display str'],
                                                board[3]['display str']))
    print('|         |         |         |')
    print(' ----------------------------- ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[4]['display str'], board[5]['display str'],
                                                board[6]['display str']))
    print('|         |         |         |')
    print(' ----------------------------- ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[7]['display str'], board[8]['display str'],
                                                board[9]['display str']))
    print('|         |         |         |')
    print(' ============================= ')
    print('| PLAYER X: {}               |'.format(str(player_x['score']).zfill(3)))
    print('| PLAYER O: {}               |'.format(str(player_o['score']).zfill(3)))
    print(' ============================= ')


def reset_board():
    global board, player_x, player_o

    board = create_board()

    player_x['marked cells'] = []
    player_o['marked cells'] = []


def mark_cell(_player, cell_pos):
    if board[cell_pos]['state'] == '-':
        board[cell_pos]['state'] = _player['name']
        board[cell_pos]['display str'] = _player['colour'] + ' {} '.format(_player['name']) + COLOUR_THEME['BOARD']
        _player['marked cells'].append(cell_pos)
# -------------------------------------------------------------------------------------
# Move Input Logic
def get_move(_player):
    while True:
        get_move_prompt = 'Enter the the position of the move of \'{}\' player from the board:'.format(_player['name'])
        print(COLOUR_THEME['GET INPUT'] + get_move_prompt + COLOUR_THEME['RESET'])
        _input = input('>> ')

        if 'quit' in _input.lower():
            end_program()

        try:
            move = int(_input)
            if 1 <= move <= 9:
                if board[move]['state'] != '-':
                    print(COLOUR_THEME['ERROR'] + 'Error: Position already occupied' + COLOUR_THEME['RESET'])
                else:
                    return move
            else:
                print(COLOUR_THEME['ERROR'] + 'Error: Enter an unoccupied position from the board (1-9)'
                      + COLOUR_THEME['RESET'])
        except ValueError:
            print(COLOUR_THEME['ERROR'] + 'Error: Enter an unoccupied position from the board (1-9)'
                  + COLOUR_THEME['RESET'])
# -------------------------------------------------------------------------------------
# Win and Tie Condition Check

def check_win(_player):
    for win_combo in WIN_COMBINATIONS:
        if win_combo[0] in _player['marked cells'] and \
                win_combo[1] in _player['marked cells'] and \
                win_combo[2] in _player['marked cells']:
            return True

    return False


def check_tie():
    for cell in board.values():
        if cell['state'] == '-':
            return False
    return True
# -------------------------------------------------------------------------------------
# Game Logic

def play_round():
    while True:
        # clear_screen()

        global current_player

        print_board()

        move = get_move(current_player)

        mark_cell(current_player, move)

        if check_win(current_player):
            # clear_screen()
            add_score(current_player)
            print_board()
            print()
            print(COLOUR_THEME['WIN'] + 'Player {} has won'.format(current_player['colour'] + current_player['name']
                                                                   + COLOUR_THEME['WIN']) + COLOUR_THEME['RESET'])
            reset_board()
            break
        elif check_tie():
            # clear_screen()
            print_board()
            print()
            print(COLOUR_THEME['TIE'] + 'Match concluded as Tie' + COLOUR_THEME['RESET'])
            reset_board()
            break

        switch_players()
# -------------------------------------------------------------------------------------
# Game Loop Logic
def ask_for_next():
    while True:
        _input = input(COLOUR_THEME['GET INPUT'] + '\n' + 'Are you ready for another Test [Y/N]:- '
                       + COLOUR_THEME['RESET']).lower()

        yes_responses = ['yes', 'y']
        no_responses = ['no', 'n']

        if _input in yes_responses:
            return True
        elif _input in no_responses:
            return False
        elif 'quit' in _input:
            end_program()
        else:
            print(COLOUR_THEME['ERROR'] + 'Error: Invalid input. Please enter one of the below responses')
            print('Affirmative responses:', ' or '.join(yes_responses))
            print('Negative responses   :', ' or '.join(no_responses) + COLOUR_THEME['RESET'])


if __name__ == '__main__':
    can_play = True
    while can_play:
        play_round()
        can_play = ask_for_next()
    end_program()
# -------------------------------------------------------------------------------------
