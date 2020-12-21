#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   In class exercise 01
def main():
#   prompt users to enter their name
    name = input("Enter your full name: ")
#   split into list
    namelist = name.split()
#   for loop in range of the number of words
    for i in range(len(namelist)):
#   get first word& capitalize
        print(namelist[i][0].capitalize(),end='.')
    print()
main()