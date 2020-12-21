#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   In class exercise 02
#   main function
def main():
#   get input from the users
    string = input("Enter a string: ")
#   call function count_lower with the parameter string, and return the vaule with number
    number = count_lower(string)
#   print the results
    print("The number of lower case letters:", number)

#   function for counting lower case letters
def count_lower(string):
#   refers count
    count = 0
#   for loop to count the lower case
    for this_letter in string:
#   islower function to determine whether it is lower or not
        if this_letter.islower():
#   if lower count + 1
            count +=1
#   return count after it finishes
    return count
main()