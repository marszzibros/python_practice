#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Exercise05: grades

#   references the numbers
userGrades = 0
highestGrade = 0
lowestGrade = 100
sumGrade = 0
averageGrade = 0
numStudent = 0

#   while loop, and whenever it is negative and over 100, it ends, resulting print('you entered the wrong...')
while userGrades >=0 and userGrades <= 100:
#   input the grade
    userGrades = int(input('Enter Grade:'))
    if userGrades >=0 and userGrades <= 100:
#   sum of the grades        
        sumGrade += userGrades
#   student counts
        numStudent +=1
#   higher number detector
        if highestGrade < userGrades:
            highestGrade = userGrades
#   hower number detector
        if lowestGrade > userGrades:
            lowestGrade = userGrades
#   average calculator
        averageGrade = sumGrade / numStudent
#   print statements
        print('highest grade: ', highestGrade,sep='')
        print('lowest grade: ', lowestGrade,sep='')
        print('your grade: ', userGrades,sep='')
        print('average of the grades: ', averageGrade,sep='')
        print('\n')
    else:
        print('You entered the wrong number')
