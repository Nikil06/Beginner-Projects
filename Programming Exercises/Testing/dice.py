'''
import random

'''
'''
 ________     __________     __________     __________     __________     __________ 
|          |   |          |   |          |   |          |   |          |   |          |
|          |   | ()       |   | ()       |   | ()    () |   | ()    () |   | ()    () |
|    ()    |   |          |   |    ()    |   |          |   |    ()    |   | ()    () |
|          |   |       () |   |       () |   | ()    () |   | ()    () |   | ()    () |
|__________|   |__________|   |__________|   |__________|   |__________|   |__________|

'''
'''
# Making the ASCII Art of Dice as shown above
dice_first_line = ' __________ '
dice_last_line  = '|__________|'
dice_L_dot  = '| ()       |'
dice_M_dot  = '|    ()    |'
dice_R_dot  = '|       () |'
dice_LR_dot = '| ()    () |'
dice_empty  = '|          |'

dice_1 = '\n'.join([dice_first_line, dice_empty, dice_empty,  dice_M_dot,  dice_empty,  dice_last_line])
dice_2 = '\n'.join([dice_first_line, dice_empty, dice_L_dot,  dice_empty,  dice_R_dot,  dice_last_line])
dice_3 = '\n'.join([dice_first_line, dice_empty, dice_L_dot,  dice_M_dot,  dice_R_dot,  dice_last_line])
dice_4 = '\n'.join([dice_first_line, dice_empty, dice_LR_dot, dice_empty,  dice_LR_dot, dice_last_line])
dice_5 = '\n'.join([dice_first_line, dice_empty, dice_LR_dot, dice_M_dot,  dice_LR_dot, dice_last_line])
dice_6 = '\n'.join([dice_first_line, dice_empty, dice_LR_dot, dice_LR_dot, dice_LR_dot, dice_last_line])

dice = {1: dice_1, 2: dice_2, 3: dice_3, 4: dice_4, 5: dice_5, 6: dice_6}
'''
'''

dice = {
    1:
""" __________
|          |
|          |
|    ()    |
|          |
|__________|
""",
    2:
""" __________
|          |
| ()       |
|          |
|       () |
|__________|
""",
    3:
""" __________
|          |
| ()       |
|    ()    |
|       () |
|__________|
""",
    4:
""" __________
|          |
| ()    () |
|          |
| ()    () |
|__________|
""",
    5:
""" __________
|          |
| ()    () |
|    ()    |
| ()    () |
|__________|
""",
    6:
""" __________
|          |
| ()    () |
| ()    () |
| ()    () |
|__________|
"""
}


# Actual Program Starts Here
# Title
print('-'*15+'DICE ROLL PROGRAM'+'-'*15)

can_play = True
roll_count = {i:0 for i in list(dice)}

while can_play:
    roll_result = random.choice(list(dice)) # Roll The Dice
    print('The Dice Lands on', roll_result) 
    print(dice[roll_result])
    roll_count[roll_result] += 1            # Increment Corresponding Roll Count
    
    user_inp = input('Enter 1 to quit:- ').lower()
    print('\n')
    if user_inp == '1':
         can_play = False
         break

print('-'*20+'REPORT'+'-'*20)
print('Total Rolls :', sum(roll_count.values()))
[print(i,'Count     :', j) for i,j in roll_count.items()]
print('-'*20+'END'+'-'*23)
'''
import random
import time


class SlotMachine:
    def __init__(self, reel_num: int, win_dict: dict):
        self.reels = [['🍒', '🍋', '🍊', '🍉', '🔔', '🍫', ' 7 ']] * reel_num
        self.win_dict = win_dict

    def spin(self):
        spin_result = ''
        for reel in self.reels:
            spin_result = spin_result + str(random.choice(reel))
        return spin_result


slot_1 = SlotMachine(3, {})

[(print(slot_1.spin()), time.sleep(.33)) for i in range(100)]

