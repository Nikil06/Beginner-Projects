import random

# Define the game code function
def gameCode(count):
    # Generate a random number between 1 and 99
    num = random.choice(range(1, 100))

    # Display the game instructions
    print('Welcome to the Guessing Game')
    print('Guess a number from 1 to 99 till u get it right')
    print()

    # Allow up to 10 attempts to guess the number
    for i in range(1, 11):
        # Prompt the user for a guess
        try:
            guess = int(input('>>'))
        except ValueError:
            print('Please enter a number.')
            continue

        # Compare the guess to the random number
        diff = guess - num

        if diff == 0:
            print(f'You got it in {i} tries!')
            count += 1
            break
        else:
            # Determine the feedback message based on the difference between the guess and the number
            feedback = {
                range(76, 100): 'Too high',
                range(51, 76): 'Still high',
                range(26, 51): 'High',
                range(1, 26): 'High but close',
                range(-25, 0): 'Low but close',
                range(-50, -25): 'Low',
                range(-75, -50): 'Still low',
                range(-99, -75): 'Too low'
            }
            for r in feedback:
                if diff in r:
                    print(feedback[r])
                    break

            count += 1

    else:
        print(f'Sorry, you didn\'t guess the number. It was {num}')

    return count


# Define the function to ask the user if they want to play again
def askForNext():
    while True:
        Input = input('\n' + "Are you ready for another Test [Y/N]:- ").upper()[0]

        if Input == 'Y':
            return True
        elif Input == 'N':
            return False
        else:
            print('Error: Invalid input. Please enter "y" or "n".')


# Run the game
if __name__ == '__main__':
    playing = True
    count = 0
    while playing:
        count = gameCode(count)
        playing = askForNext()
        print()

    print('Thank you for playing!')
