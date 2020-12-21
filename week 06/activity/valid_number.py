#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   task 02: valid number checker

#   main function
def main():
    low = int(input('Enter lower value: '))
    high = int(input('Enter higher value: '))
#   call the function
    num = get_valid_number(low,high)
    print('The valid number is', num)

#   get_valid_number function with lowest and highest number
def get_valid_number(low,high):
#   user enter the valid number
    validValue = int(input('Enter a Value: '))
#   if not, while loop until the user enter the valid number
    while not(validValue > low and validValue < high):
        validValue = int(input('Invalid number! Enter a Value: '))
#   return the valid number that user entered
    return validValue
main()