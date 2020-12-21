#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   find the biggest number using if condition

#   Enter the three integer
num1 = int(input('First number: '))
num2 = int(input('Second number: '))
num3 = int(input('Thrid number: '))

#   Use bubble sort...
#   sorting variable 'sorting_number'..

if num1 < num2:
    sorting_number = num1
    num1 = num2
    num2 = sorting_number
    if num2 < num3:
        sorting_number = num2
        num2 = num3
        num3 = sorting_number
        if num1 < num2:
            sorting_number = num1
            num1 = num2
            num2 = sorting_number

elif num2 < num3 :
    sorting_number = num2
    num2 = num3
    num3 = sorting_number
    if num1 < num2 :
        sorting_number = num1
        num1 = num2
        num2 = sorting_number

#   print the results
print('Descending order:', num1, num2, num3, sep='  ')
