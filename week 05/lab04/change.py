#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB 04-01: Exchange coins

#   money constants
QUARTER = 25
DIME = 10
NICKEL = 5

#   main function
def main():
#   centChange: input variable
#   check: if it is valid or not if valid it refers 0, if not it refers 1
    centChange = 0
    check = 0
#   while loop that runs until the input number is valid
    while not(centChange <= 99 and centChange >= 1):
#   call print function and after input
        print_input(check)
        centChange = int(input())
#   if the input number is invalid, call the function again so that it prints invalid
        if not(centChange <= 99 and centChange >= 1):
            check = 1
            print_input(check)
            check = 0
#   call the calculation function
    exchange(centChange)

#   print function
def print_input(check):
#   check == 0 : normal condition (when we have to enter the number)
    if check == 0:
        print('How much change do you need in cents? ',end='')
#   check == 1 : print it is invalid
    elif check == 1:
        print('The change must be between 1 cent and 99 cents!')

#   calculation function
def exchange(centChange):
#   quarter calculate
    quarterNum = centChange // QUARTER
    centChange %= QUARTER
#   dime calculate
    dimeNum = centChange // DIME
    centChange %= DIME
#   nickel calculate
    nickelNum = centChange // NICKEL
#   penny calculate
    pennyNum = centChange % NICKEL
    
#   calculate final results
    print(quarterNum,'Quarters')
    print(dimeNum,'Dimes')
    print(nickelNum,'Nickels')
    print(pennyNum,'Pennies')

#   call the main function
main()
