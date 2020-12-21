#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup task 03: file data processing

#   This program writes data to a text file
def main():
    highScore = 0
    lowScore = 100
    total = 0
    numCount = 0 
#   open file named firstfile.txt in read mode
    readfile = open('scores.txt','r')

#   for loop for reading file 'scores.txt'
    for line in readfile:
#   read without \n
        score = int(line.rstrip('\n'))
#   find the highscore and lowscore by comparing
        if score > highScore:
            highScore = score
        if score < lowScore:
            lowScore = score
#   count the number of grades
        numCount += 1
#   add the scores
        total += score

#   calculate average
    average = format(total / numCount,'.2f')
#   close readfile 'stats.txt'
    readfile.close()

#   open file named stats.txt in write mode    
    writefile = open('stats.txt','w')
    writefile.write('The Exam high score is : ' + str(highScore) + '\n')
    writefile.write('The Exam low score is  : ' + str(lowScore) + '\n')
    writefile.write('The Exam average is    : ' + str(average) + '\n')

#   close writefile '.txt'       
    writefile.close()

#   call the main function
main()
