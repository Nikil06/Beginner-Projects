# -------------------------------------------------------------------------------------
# Defined Constants
WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]
# -------------------------------------------------------------------------------------
# Player Structure
player_x = {'name': 'X',
            'marked cells': [],
            'score': 0}

player_o = {'name': 'O',
            'marked cells': [],
            'score': 0}

current_player = player_x


def add_score(player):
    player['score'] += 1


def switch_players():
    global current_player, player_x, player_o
    if current_player == player_x:
        current_player = player_o
    elif current_player == player_o:
        current_player = player_x


# -------------------------------------------------------------------------------------
# Cell Structure
def create_cell(pos):
    return {
        'pos': pos,
        'state': '-',
        'display str': '[{}]'.format(pos)
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
    print(' ============================= ')
    print('|         TIC-TAC-TOE         |')
    print(' ============================= ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[1]['display str'], board[2]['display str'], board[3]['display str']))
    print('|         |         |         |')
    print(' ----------------------------- ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[4]['display str'], board[5]['display str'], board[6]['display str']))
    print('|         |         |         |')
    print(' ----------------------------- ')
    print('|         |         |         |')
    print('|   {}   |   {}   |   {}   |'.format(board[7]['display str'], board[8]['display str'], board[9]['display str']))
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
        board[cell_pos]['display str'] = ' {} '.format(_player['name'])
        _player['marked cells'].append(cell_pos)


# -------------------------------------------------------------------------------------
# Move Input Logic
def get_move(_player):
    while True:
        print('Enter the the position of the move of \'{}\' player from the board:'.format(_player['name']))
        _input = input('>> ')

        if 'quit' in _input.lower():
            quit()

        try:
            move = int(_input)
            if 1 <= move <= 9:
                if board[move]['state'] != '-':
                    print('Error: Position already occupied')
                else:
                    return move
            else:
                print('Error: Enter an unoccupied position from the board (1-9)')
        except ValueError:
            print('Error: Enter an unoccupied position from the board (1-9)')


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
            print('Player {} has won'.format(current_player['name']))
            reset_board()
            break
        elif check_tie():
            # clear_screen()
            print_board()
            print()
            print('Match concluded as Tie')
            reset_board()
            break

        switch_players()


# -------------------------------------------------------------------------------------
# Game Loop Logic
def ask_for_next():
    while True:
        _input = input('\n' + 'Are you ready for another Test [Y/N]:- ').lower()

        yes_responses = ['yes', 'y']
        no_responses = ['no', 'n']

        if _input in yes_responses:
            return True
        elif _input in no_responses:
            return False
        elif 'quit' in _input:
            quit()
        else:
            print('Error: Invalid input. Please enter one of the below responses')
            print('Affirmative responses:', ' or '.join(yes_responses))
            print('Negative responses   :', ' or '.join(no_responses))


if __name__ == '__main__':
    can_play = True
    while can_play:
        play_round()
        can_play = ask_for_next()
# -------------------------------------------------------------------------------------
