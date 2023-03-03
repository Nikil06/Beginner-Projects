import random

choices = ('Rock', 'Paper', 'Scissor')
p_score = 0
ai_score = 0


def getAiChoice():
    return random.choice(choices)


def getUserChoice():
    while True:
        p_input = input('Player  : ').lower().capitalize()

        for choice in choices:
            if p_input == choice:
                return choice
        else:
            print('Enter Valid Input')


def playerWon():
    global p_score
    p_score += 1
    print('-'*10 + 'You Won' + '-'*10)


def playerLost():
    global ai_score
    ai_score += 1
    print('-'*10 + 'You Lost' + '-'*10)


def playerTied():
    print('-'*10 + 'You Tied' + '-'*10)


def gameCode():
    p_choice = getUserChoice()
    ai_choice = getAiChoice()

    print(f'Computer: {ai_choice}')

    if p_choice == ai_choice:
        playerTied()
    elif p_choice == choices[0] and ai_choice == choices[2]:
        playerWon()
    elif p_choice == choices[1] and ai_choice == choices[0]:
        playerWon()
    elif p_choice == choices[2] and ai_choice == choices[1]:
        playerWon()
    else:
        playerLost()

    print(f'Scores: Player - {p_score}, AI - {ai_score}')


def askForNext():
    while True:
        print('Enter "1" to Quit')
        p_input = input('>>')

        if p_input == '1':
            return False
        else:
            return True


if __name__ == '__main__':
    print('Welcome to the Arena\n')

    playing = True

    while playing:
        gameCode()
        playing = askForNext()