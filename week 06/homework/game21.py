#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW06-02 random games
import random

#   Global constants
HIT = 21
INITIAL = 0
DICE_MIN = 1 
DICE_MAX = 6
YES = 'y'
NO = 'n'

#   main function
def main():
#   refer the variable to 0
    userSum = INITIAL
    comSum = INITIAL

#   call if the user want to do it or not
    YorN = get_response()

#   if YES enter, and only if userSum is lower than 21
    while YorN == YES and userSum < HIT:
#   roll dices (USER) and sum it
        dice1, dice2 = roll_dice()
        userSum = userSum + (dice1 + dice2)
#   roll dices (COMPUTER) and sum it       
        dice1, dice2 = roll_dice()
        comSum = comSum + (dice1 + dice2)
#   print just userSum        
        print('points:',userSum)

#   ask if user want to keep going        
        if userSum < HIT:
            YorN = get_response()

#   print user and computer's point at the end of the game
    print('User\'s point:', userSum)
    print('Computer\'s point:', comSum)    

#   if both exceed => tie game
    if userSum > HIT and comSum > HIT:
        print('Tie Game!')
#   if only the user exceed => computer win
    elif userSum > HIT and comSum <= HIT:
        print('Computer wins')
#   if only the computer exceed => user win
    elif userSum <= HIT and comSum > HIT:
        print('User wins')
#   if same
    elif userSum <= HIT and comSum <= HIT:
#   finish it before it starts => tie game        
        if userSum == INITIAL and comSum == INITIAL:
            print('Tie Game!')
#   if both did not reach 21 => computer win
        else:
            print('Computer wins!')
    
#   random dice function
def roll_dice():
    dice1 = random.randint(DICE_MIN,DICE_MAX)
    dice2 = random.randint(DICE_MIN,DICE_MAX)
    return dice1, dice2

#   ask if the user wants to keep doing
def get_response():
    YorN = 'a'
    while not (YorN == YES or YorN == NO):
        YorN = input('Do you want to roll? ')
    return YorN
main()