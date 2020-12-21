#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB08 - reverse.py

#   main function
def main():
#   ask user the letter that wants to reverse
    reverse_words = input("What would you like to reverse? ")
#   call the function and return back the value
    print(reverse_string(reverse_words))

#   function for reversing strings    
def reverse_string(reverse_words):
#   refers the string variable for reversed words
    changing_words = ''
#   for loop to reverse words
    for i in range(len(reverse_words) - 1, -1, -1):
        changing_words += reverse_words[i]
#   return
    return changing_words
#   call main function
main()