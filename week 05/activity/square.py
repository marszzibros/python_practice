#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   square.py

#   main function
def main():
    num = int(input('Enter a number: '))
    square_nums(num)
#   square_nums function
def square_nums(num):
#   square
    square = num ** 2
#   print
    print('The square of',num,'is',square)

main()
