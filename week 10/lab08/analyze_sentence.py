#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB08 - analyze.sentence.py

#   main function
def main():
#   refers the value
    total = 0
    averageLen = 0
    sentence = ''
#   if there is a word 'quit' end the program
    while sentence.find('quit') == -1:
#   try dividing
        try:  
#   prompt users to enter the sentence
            print("Please type a sentence. When you are done entering sentences")
            sentence = input("enter a stence containing the word quit:")
#   split the string so that program can count the words
            wordList = sentence.split()
#   check the length of the words and add total
            for i in range(0,len(wordList)):
                total += len(wordList[i])
#   get average lengths of the word
            averageLen = total/len(wordList)
#   if the user did not enter the word, it is impossible to divide, so make exception
        except:
            print("you should at least enter a word! Try it again!")
#   print the results
        else:
            print("That sentence contains", len(wordList), "words with an average word length of", format(averageLen,'.1f'))
#   make total 0 to re-use it        
        finally:
            total = 0
main()
