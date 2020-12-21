#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW07-01 grade check

#   global constants for grading
QUIZ = 0.05
LAB = 0.15
INCLASS_ACT = 0.05
HW_ASSIGN = 0.25
EXAM = 0.4
FINAL_PRO = 0.1

#   global constants for letter grading
A_MAX = 100
A_MIN = 90
B_MIN = 80
C_MIN = 70
D_MIN = 60

#   main function
def main():
#   variables set
    inputFile = ''
    gradeFile = ''
    letterFile = ''
    studentNum = 0
    totalScore = 0
    minGrade = 100
    maxGrade = 0
    stuA = 0
    stuB = 0
    stuC = 0
    stuD = 0
    stuF = 0
    letter = ''

#   call 'get_file_name(inputFile, gradeFile, letterFile)' for file name


#   opening files
#   exception might occur while it opens the file
    try:
        inputFile, gradeFile, letterFile = get_file_name(inputFile, gradeFile, letterFile)
        getGrade = open(inputFile, 'r') 
    except:
        print('End Program')
    else:
        try:
            gradeIndividual = open(gradeFile, 'w')
        except IOError:
            print('End Program')
            getGrade.close()
        else:
            try:
                gradeLetter = open(letterFile,'w')
            except IOError:
                print('End Program')
                getGrade.close()
                gradeIndividual.close()
            else:
    
#   get first name + delete \n using rstrip
                name = getGrade.readline()
                name = name.rstrip('\n')
#   while loop until there is no data
                while name != '':
#   read data one by one 'readline' + rstrip('\n') + change to float
                    try:
#   if there is invalid grade, we should skip a student
#   so I readline all the grade as str
                        per_quiz = getGrade.readline()
                        per_lab = getGrade.readline()
                        per_inclass = getGrade.readline()
                        per_hw = getGrade.readline()
                        per_exam = getGrade.readline()
                        per_finalProject = getGrade.readline()
#   and change it to float, and if it has error, exception will print "skip"
                        per_quiz = float(per_quiz.rstrip('\n'))
                        per_lab = float(per_lab.rstrip('\n'))
                        per_inclass = float(per_inclass.rstrip('\n'))
                        per_hw = float(per_hw.rstrip('\n'))
                        per_exam = float(per_exam.rstrip('\n'))
                        per_finalProject = float(per_finalProject.rstrip('\n'))
                    except:
                        print('Invalid grade, skip scoring')
#   call function get_total_grade(per_quiz, per_lab, per_inclass, per_hw, per_exam, per_finalProject) to get an one's total grade
                    else:
                        total = get_total_grade(per_quiz, per_lab, per_inclass, per_hw, per_exam, per_finalProject)

#   call determine_grade(total) determine the letter grade
                        letter = determine_grade(total)

#   count letters
                        if letter == 'A':
                            stuA += 1
                        elif letter == 'B':
                            stuB += 1 
                        elif letter == 'C':
                            stuC += 1
                        elif letter == 'D':
                            stuD += 1
                        else:
                            stuF += 1
#   write to the individual grade file with a format of (name grade)
                        gradeIndividual.write(name + ' ' + letter + '\n')
       
#   find minimum grade & maximum grade
                        if minGrade > total:
                            minGrade = total
                        if maxGrade < total:
                            maxGrade = total
#   total score for average
                        totalScore += total
#   count a number of students
                        studentNum += 1
#   get a name
                    finally:
                        name = getGrade.readline()
                        name = name.rstrip('\n')

#   read next name in the given txt file

#   average calulation
                try:
                    average = float(format(totalScore/studentNum,'.2f'))
                except:
                    print('you cannot divide by 0')
#   write an overall grade for all students in a selected file
                else:
                    gradeLetter.write('Average grade: ' + str(average) + ' ' + determine_grade(average) + '\n')
                    gradeLetter.write('Minimum grade: ' + str(format(minGrade,'.2f')) + ' ' + determine_grade(minGrade) + '\n')
                    gradeLetter.write('Maximum grade: ' + str(format(maxGrade,'.2f')) + ' ' + determine_grade(maxGrade) + '\n')
                    gradeLetter.write('Letter grade histogram\n')
#   file close
                    gradeLetter.close()
                    
#   call histogram to draw histogram on a given txt file
#   parameter: filename, and the counts of letter grade from A to F 
                    histogram(letterFile ,'A\'s: ', stuA)
                    histogram(letterFile ,'B\'s: ', stuB)
                    histogram(letterFile ,'C\'s: ', stuC)
                    histogram(letterFile ,'D\'s: ', stuD)
                    histogram(letterFile ,'F\'s: ', stuF)
#   file close        
                    getGrade.close()
                    gradeIndividual.close()

#   function for total grade using constants above
def get_total_grade(per_quiz, per_lab, per_inclass, per_hw, per_exam, per_finalProject):
    totalGrade = (QUIZ * per_quiz) + (LAB * per_lab) + (per_inclass * INCLASS_ACT) + (per_hw * HW_ASSIGN) + (per_exam * EXAM) + (per_finalProject * FINAL_PRO)
#   return calculated totalGrade    
    return totalGrade

#   function for asking user for the file name they want to read and write    
def get_file_name(inputFile, gradeFile, letterFile):
#   try to open a file
    try:
        inputFile = input('What is the name of the file to use for grade input? ')
        openTest = open(inputFile,'r')
        openTest.close()
    except IOError:
        print('Could not open input file. Exiting now')
    else:
        try:
            gradeFile = input('What is the name of thefile to use for outputting individual student grades? ')
            openTest = open(gradeFile,'a')
            openTest.close()
        except IOError:
            print('Could not open input file. Exiting now')
        else:
            try:
                letterFile = input('What is the name of the file to use for Grade report? ')
                openTest = open(letterFile,'a')
                openTest.close()
            except IOError:
                print('Could not open input file. Exiting now')
    finally:
#   return it back
        return inputFile, gradeFile, letterFile

#   function for determining a letter grade
def determine_grade(score):
#   determine the letter grade depends on the grade table
    if score <= A_MAX and score >= A_MIN:
        return 'A'
    elif score < A_MIN and score >= B_MIN:
        return 'B'
    elif score < B_MIN and score >= C_MIN:
        return 'C'
    elif score < C_MIN and score >= D_MIN:
        return 'D'
    else:
        return 'F'

#   function for drawing a histogram
def histogram(letterFile, statement ,count):
#   re-open a file using 'a' mode
    gradeLetter = open(letterFile,'a')

#   write a statement for histogram
#   printing a number of A using *    
    gradeLetter.write(statement)    
    for i in range(0,count):
        gradeLetter.write('*')
    gradeLetter.write('\n')       

#   close a file    
    gradeLetter.close()         

#   call main function
main()
