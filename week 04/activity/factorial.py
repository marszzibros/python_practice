#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Exercise03: Factorial

#   print the table
n = int(input('Enter a number: '))

#   reference sumNumber 1
factorialNumber = 1

#   validity check
if n >= 0:
#   for until n+1 since it does not include n
    for i in range(1,n+1):
#   multiply as it goes
        factorialNumber *= i
#   print after it is done
    print('The factorial of ', n, ' is ', factorialNumber, sep='' )
#   display that it is a wrong number
else:
    print('you enter the wrong number')

