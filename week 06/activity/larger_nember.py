#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   task 03: larger number checker

#   main function
def main():
    for i in range(0, 3):
        num = int(input('enter a number: '))
#   on the first enter, there is no specific comparison, so I will put Largenum as a first entered number
        if i == 0:
            LargeNum = num
#   call the larger function
        largeNum = larger(num, LargeNum)
#   print
    print('The largest number is',largeNum)

#   function larger 
def larger(num1, num2):
#   if the number that just entered is small, return num2
    if num1 < num2:
        return num2
#   unless, return num1
    else:
        return num1

main()