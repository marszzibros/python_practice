#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Lab04 : number guessing game

#   To use random function, import document 'random'
import random

#   Constant maximum try
MAX_TRIES = 5

#   To enter the while loop, referece the variable again as 'y'
again = "y"

#   If and only if again is 'y'
while again == "y" or again == "Y":

#   When it starts again, it need to be refreshed
    enterNum = 0
    numCount = 0

    print('I am thinking of a number between 1 and 100 \nYou have 5 tries to guess it. Good luck!')
#   Create the random value    
    ranNum = random.randint(1, 100)
    while enterNum != ranNum and numCount < MAX_TRIES:
#   Enter the number
        enterNum = int(input('Enter a guess between 1 and 100: '))
#   If it is an invalid value, enter the loop so that they can reenter.
        while not(enterNum > 0 and enterNum < 101):
#   Print invalid number
            if enterNum <= 0 or enterNum > 101:
                print('Invalid Input')
#   Re-enter the number
            enterNum = int(input('Enter a guess between 1 and 100: '))

#   Count the number of attempts
        numCount += 1

#   Decide whether it is high or low or right
        if numCount != MAX_TRIES or enterNum == ranNum:
            if enterNum > ranNum:
                print('Too high')
            elif enterNum < ranNum:
                print('Too low')
            else:
                print('Congratulations! You guessed it in', numCount, 'tries')
        else:
            print('Sorry, you\'re out of tries. The number was', ranNum)
#   Ask the user if they want to play again
    again = input('Play again? (Y or N) ')


            