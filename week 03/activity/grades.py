#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Activity 02: determine the grades

#   input the grades
grade = int(input('Enter your grade: '))
#   using if condition (90-100)
if grade >= 90 and grade <= 100:
    print('Your grade is A')
#   elif(80-89)
elif grade >= 80 and grade <= 89:
    print('Your grade is B')
#   elif(70-79)
elif grade >= 70 and grade <= 79:
    print('Your grade is C')    
#   elif(60-69)
elif grade >= 60 and grade <= 69:
    print('Your grade is D')
#   else
else:
#   grade over 100 or less than 0 might regard as 'invalid'    
    if grade > 100 or grade < 0:
        print('invalid')
#   or it is just F (the score is under 60) 
    else:
        print('Your grade is F')

