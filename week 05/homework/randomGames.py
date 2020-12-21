#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW05-01 random games
import random

#   main function
def main():
#   to enter the while, I refer the variable options to 0
    options = 0
#   while loop operates until the user enters 3
    while options != 3:
#   when it executes the loop, options should be refreshed
        options = 0
#   options 1 to 3
        while not(options >= 1 and options <=3):
#   call "pringMenu" function, and print the options          
            printMenu()
            options = int(input("What option do you choose? "))
            if not(options >= 1 and options <=3):
                print("Please Pick an option from the menu!")
#   if the user chooses 1, it goes to dice game
        if options == 1:
            rollingDice()
#   if the user chooses 2, it goes to bingo game
        elif options == 2:
            bingoDraw()
#   A function that prints the menu of options for the screen
def printMenu():
    print("Use the numbers to select an option")
    print("1: Roll some dice!")
    print("2: Play some Bingo!")
    print("3: Quit")

#   A function that simulates the rolling of dice
def rollingDice():
#   refer the number before it enters the while loop
    diceNum = 0
    diceSides = 0
    totalVal = 0
#   until a user inputs the valid number (>0)
    while not(diceNum > 0):
        diceNum=int(input('How many dice do you want to roll? '))
        if diceNum <= 0:
            print('Number of dice must be greater than 0!')
    while not(diceSides > 0):
        diceSides=int(input('How many sides are on each die? '))
        if diceSides <= 0:
            print('Number of sides must be greater than 0!')

#   using for loop and random function, generate the random number (diceNum times)
    for i in range(1, diceNum + 1):
#   1 ~ diceSides
        diceVal = random.randint(1,diceSides)
        totalVal += diceVal 
        print("Roll number", i, "is", diceVal)
    print("Total of all rolls is:", totalVal)

#   A funnction taht simulates a random Bingo draw
def bingoDraw():
#   generate the random number for the letter
#   B == 1, I == 2, N == 3, G == 4, O == 5
    bingoLetter = random.randint(1,5)

#   print Letter+bingoNum(random number) with sep=''
#   if the random num is 1... (B), generate the number between 1 and 15
    if bingoLetter == 1:
        bingoNum = random.randint(1,15)
        print("The next number in Bingo is: B", bingoNum, sep='')
#   if the random num is 2... (I), generate the number between 16 and 30
    elif bingoLetter == 2:
        bingoNum = random.randint(16,30)
        print("The next number in Bingo is: I", bingoNum, sep='')
#   if the random num is 3... (N), generate the number between 31 and 45
    elif bingoLetter == 3:
        bingoNum = random.randint(31,45)
        print("The next number in Bingo is: N", bingoNum, sep='')
#   if the random num is 4... (G), generate the number between 46 and 60
    elif bingoLetter == 4:
        bingoNum = random.randint(46,60)
        print("The next number in Bingo is: G", bingoNum, sep='')
#   if the random num is 5... (O), generate the number between 61 and 75
    elif bingoLetter == 5:
        bingoNum = random.randint(61,75)
        print("The next number in Bingo is: O", bingoNum, sep='')

#   call the main function
main()
