#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   find the biggest number using if condition

#   Constant(DOZENS) = 12
DOZENS = 12

#   print the explanation
print('This program will determine the required number of 1-dozen egg cartons')

#   input the number of the eggs that the users collected
collect_eggs=int(input('How many eggs did you collet today? '))
#   if positive, go to the next step: calculation
if collect_eggs >= 0:
#   do the devision(/) and left over(%)
    egg_cartons = collect_eggs / DOZENS
    left_over = collect_eggs % DOZENS
    print('We will pack your ', collect_eggs, ' eggs in ', int(egg_cartons), ' cartons.', sep='')
    print('There will be ', left_over, ' eggs left over.', sep='')

#   if negative, print 'you cant do this' and quit the program
else:
    print('Your value cannot be negative.')
