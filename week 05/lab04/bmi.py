#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB 04-02: BMI calculator

#   Constants
MIN_HEIGHT = 48
MAX_HEIGHT = 96
MIN_WEIGHT = 75
MAX_WEIGHT = 1000
BMINUM = 703

#   main function
def main():
#   weight and height refers to 0 so that program can enter the while loop
#   check: if it is valid or not if valid it refers 0, if not it refers 1
#   WorH: if 0 it is weight, if 1, it is height
    weight = 0
    height = 0
    check = 0
#   weight, while loop to run until the valid number   
    WorH = 0
    while not(weight <= MAX_WEIGHT  and weight >= MIN_WEIGHT):
#   call print function
        print_input(WorH, check)
        weight = int(input())
#   if the input number is invalid, call the function again so that it prints invalid
        if not(weight <= MAX_WEIGHT  and weight >= MIN_WEIGHT):
            check = 1
            print_input(WorH, check)
            check = 0

#   height, while loop to run until the valid number   
    WorH = 1
    while not(height <= MAX_HEIGHT  and height >= MIN_HEIGHT):
#   call print function
        print_input(WorH, check)
        height = int(input())
#   if the input number is invalid, call the function again so that it prints invalid
        if not(height <= MAX_HEIGHT  and height >= MIN_HEIGHT):
            check = 1
            print_input(WorH, check)
            check = 0
#   call the callculation function
    display_BMI(weight,height)

#   print function
def print_input(WorH,check):
#   if WorH == 0 : weight 
#   if WorH == 1 : height
#   if check 0 : print enter weight or height
#   if chekc 1 : print "invalid"
    if WorH == 0:
        if check == 0:
            print('Enter weight: ',end='')
        elif check == 1:
            print('Invalid weight try again!') 
    elif WorH == 1:
        if check == 0:
            print('Enter height: ',end='')
        elif check == 1:
            print('Invalid height try again!') 

#   bmi calculation function
def display_BMI(weight, height):
#   bmi calculation
    bmi = float(format(weight * (BMINUM / (height ** 2)),'.1f'))
#   if condition
    if bmi < 18.5:
        print('BMI =',bmi,'underweight')
    elif bmi <= 24.9 and bmi >= 18.5:
        print('BMI =',bmi,'normal')
    elif bmi <= 29.9 and bmi >= 25:
        print('BMI =',bmi,'overweight')
    else:
        print('BMI =',bmi,'obese')

#   call main function
main()
