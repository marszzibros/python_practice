#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   In class exercise 03
def main():
    total = 0
#   enter value
    value = input("Enter digits without spaces: ")
#   get splited value through for loop    
    for i in value:
#   fetch the value
        print(i)
#   find the total of the digit
        total+=int(i)
#   print the total
    print("The total is:", total)
main()