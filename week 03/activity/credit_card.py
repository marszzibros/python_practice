#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Activity 03: credit card approval

#   input the age and the credit score
age = int(input('Enter age: '))
credit_score = int(input('Enter credit score: '))

#   use if condition (credit >= 700 and age <=25)
if credit_score >= 700 and age >= 25:
    print('Approved')

#   or display not approved
else:
    print('Not Approved')
#   the reason why you are not approved (credit)    
    if credit_score < 700 and not(age < 25): 
        print('Your credit score is too low.')
#   the reason why you are not approved (age)           
    elif not(credit_score < 700) and age < 25:
        print('You are too young.') 
#   the reason why you are not approved (both age and credit)                
    else:
        print('You are too young AND your credit is too low')


