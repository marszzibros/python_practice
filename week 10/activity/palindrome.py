#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   In class exercise 04

def main():
    palindrome = False
    words = input("Enter words!")
    if len(words) % 2 == 0:
        palindrome = even(words)
    elif len(words) % 2 != 0:
        palindrome = odd(words)
    
    if palindrome == True:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome!")        
def odd(words):
    count = 0
    wordcount = 0
    while count != (len(words) // 2):
        if words[count] == words[len(words) - count - 1]:
            wordcount += 1
        count += 1 
    if wordcount == len(words) // 2:
        return True
    else:
        return False 
def even(words):
    count = 0
    wordcount = 0
    while count != (len(words) // 2):
        if words[count] == words[len(words) - count - 1]:
            wordcount += 1
        count += 1 
    if wordcount == len(words) / 2:
        return True
    else:
        return False 
main()
