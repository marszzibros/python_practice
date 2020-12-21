#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB05 : money exchange to canadian dollars

#   global constant
RATE = 1.33

#   main function
def main():
#   print the statements    
    print('Let\'s convert your US Dollars to Canadian Dollars')
#   input us dollars, as suggested, I do not need to validate the number    
    usDollarAmount = float(input('Enter the value of your US dollars: '))

#   call the function and at the same time print the calculated moeny
    canadian_Dollar = usd2can(usDollarAmount)
    print('This amount is worth $', format(canadian_Dollar,'.2f'),'Canadian dollars.')

#   exchanging function
def usd2can(usDollarAmount):

#   rate * us dollar = canadian dollars 
    return RATE * usDollarAmount

#   call main function
main()