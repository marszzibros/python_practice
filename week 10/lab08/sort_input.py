#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB08 - analyze.sentence.py

#   main function
def main():
#   refers the variable
    total = 0
    inputList = []
#   to enter the while loop, append with any letter(delete later)
    inputList.append(0)
#   while loop until the user enters 'q' 
    while inputList[len(inputList) - 1] != 'q':
#   get input until the user enters 'q', and append it into a list
        inputList.append(input("Enter any value(numbers, text or a mix.) Enter q  when you are done entering values: "))
#   delete the first 0 since it is not a value that user enterss    
    del(inputList[0])
#   delete 'q'
    del(inputList[len(inputList) - 1])
#   print number and sum
    print("You entered the following numbers:")
#   find number using for loop
    for i in range(0,len(inputList)):
#   use isdigit() method to find number
        if inputList[i].isdigit():
            total += int(inputList[i])
            print(inputList[i])
#   print results
    print("The sum of those numbers is:", total)
#   print words
    print("You entered the following words")
#   find words using for loop
    for i in range(0,len(inputList)):
#   use isalpha()
        if inputList[i].isalpha():
            print(inputList[i])
#   print results     
    print("You entered the following values which contain a mix of numbers, letters, and characters:")
#   find neither cases
    for i in range(0,len(inputList)):
#   find it using not(isalpha, and isdigit method)
        if not(inputList[i].isalpha() or inputList[i].isdigit()):
            print(inputList[i])
#   call main funcion       
main()
