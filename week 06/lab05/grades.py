#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB05 : grades determine table

#   global constant
A_MAX = 100
A_MIN = 90
B_MAX = 89
B_MIN = 80
C_MAX = 79
C_MIN = 70
D_MAX = 69
D_MIN = 60
SCORENUM = 5

#   main function
def main():
#   to enter the while loop, set the value as -1
    score1 = -1
    score2 = -1
    score3 = -1
    score4 = -1
    score5 = -1
#   enter the number and at the same time check the validity
    while not(score1 <= 100 and score1 >= 0):
        score1 = int(input('Enter score 1: '))
        if not(score1 <= 100 and score1 >= 0):
            print('Invalid score! please enter the score between 0 to 100')
    while not(score2 <= 100 and score2 >= 0):
        score2 = int(input('Enter score 2: '))
        if not(score2 <= 100 and score2 >= 0):
            print('Invalid score! please enter the score between 0 to 100')
    while not(score3 <= 100 and score3 >= 0):        
        score3 = int(input('Enter score 3: '))
        if not(score3 <= 100 and score3 >= 0):        
            print('Invalid score! please enter the score between 0 to 100')
    while not(score4 <= 100 and score4 >= 0):
        score4 = int(input('Enter score 4: '))
        if not(score4 <= 100 and score4 >= 0):
            print('Invalid score! please enter the score between 0 to 100')
    while not(score5 <= 100 and score5 >= 0):
        score5 = int(input('Enter score 5: '))
        if not(score5 <= 100 and score5 >= 0):
            print('Invalid score! please enter the score between 0 to 100')    

#   print the table
    print('Scores \t     numeric grade  letter grade')
    print('-----------------------------------------')
#   call the function 'determine_grade' with the input of the score and then print
    print('score 1:',format(score1,'11d'),'\t\t',determine_grade(score1))
    print('score 2:',format(score2,'11d'),'\t\t',determine_grade(score2))
    print('score 3:',format(score3,'11d'),'\t\t',determine_grade(score3))
    print('score 4:',format(score4,'11d'),'\t\t',determine_grade(score4))
    print('score 5:',format(score5,'11d'),'\t\t',determine_grade(score5))

#   call the 'calc_average' with the five scores that user has entered
    meanScore = calc_average(score1, score2, score3, score4, score5)

#   print the average score with the letter grade determined by 'determine_grade' function
    print('-----------------------------------------')
    print('Average score:',format(meanScore, '5.1f'),'\t\t',determine_grade(meanScore))

#   dorm choosing function function
def determine_grade(score):

#   determine the letter grade depends on the grade table
    if score <= A_MAX and score >= A_MIN:
        return 'A'
    elif score <= B_MAX and score >= B_MIN:
        return 'B'
    elif score <= C_MAX and score >= C_MIN:
        return 'C'
    elif score <= D_MAX and score >= D_MIN:
        return 'D'
    else:
        return 'F'

#   calculate the averages
def calc_average(score1, score2, score3, score4, score5):
    scoreSum = score1 + score2 + score3 + score4 + score5
#   return the average (total sum / 5(the number of the scores that user entered))
    return scoreSum / SCORENUM

#   call main function
main()