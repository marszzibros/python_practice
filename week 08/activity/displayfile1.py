#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup task 02

#   This program writes data to a text file
def main():
#   open file named firstfile.txt in read mode
    readfile = open('firstfile.txt','r')

#   for loop to print three statements
    for line in readfile:
#   print without \n        
        print(line.rstrip('\n'))
    
#   close the function    
    readfile.close()
#   call the main function
main()
