#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup task 01

#   This program writes data to a text file
def main():
#   open file named firstfile.txt in write mode
    outfile = open('firstfile.txt','w')

#   Write your name to firstfile.txt
    outfile.write('JayHwasung Jung\n')

#   Write your Major to firstfile.txt
    outfile.write('Computer Science\n')
    
#   Write your hobbies to firstfile.txt
    outfile.write('I like to play any kinds of sports\n')

#   Close the file
    outfile.close()

#   call the main function
main()
