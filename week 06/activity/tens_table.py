#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   task01: ten times multiplication table

#   main function
def main():
    for i in range(10,101,10):
#   using format, make the table
        print(format(i,"8d"),format(times_ten(i),"8d"))

#   times_ten function with num variable
def times_ten(num):

#   return the value with 10 times
    return num * 10

main()