#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW04-01: Creating the multiplication table

#   Enter the starting value
numStart = int(input("Enter a positive starting value < 1000: "))
#   if not 0 < starting value < 1000, re-enter
while not(numStart > 0 and numStart < 1000):
    print(numStart,' is not a valid choice, try again')
    numStart = int(input("Enter a positive starting value < 1000: "))

#   Enter the ending value
numEnd = int(input("Enter a positive ending less than 1000 and greater than the starting value: "))
#   if not starting value < ending value < 1000, re-enter
while not(numEnd > numStart and numEnd < 1000):
    print(numEnd,' is not a valid choice, try again')
    numEnd = int(input("Enter a positive ending less than 1000 and greater than the starting value: "))

#   Print the blank space before printing starting number (two times bigger than the normal space...)(20)
print(format(numStart,'20d'),end='')

#   Print the other space (10)
for i in range(numStart+1, numEnd+1):
    print(format(i,"10d"), end='')
#   Next line
print('\n')

#   Creating the multiplication table (nested loop)
for i in range(numStart, numEnd+1):
#   Printing rows' heading
    print(format(i,'10d'), end='')

    for j in range(numStart, numEnd+1):
#   Calculate and Print the results
        print(format(i * j, "10d"),end='')
#   Next line
    print('\n')











    