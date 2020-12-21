#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Calculate Kilograms to Newtowns

#   Constant NEWTONS
NEWTONS = 9.8

#   input Kilograms
object_mass = int(input('Enter the object\'s mass in kilograms: '))

#   if condition.. whether it is more than 0 or not
if object_mass >= 0:
    
#   if mass >= 0, calculate the wieght
    object_weight = object_mass * NEWTONS

#   if weight > 500, print "you are too heavy"
    if object_weight > 500:
        print('Object Weight: ', format(object_weight,' .2f'),' newtons', sep='')
        print('The object is too heavy. It weighs more than 500 newtons.')
        
#   if weight < 100, print "you are too light"
    elif object_weight < 100:
        print('Object Weight: ', format(object_weight,' .2f'),' newtons', sep='')
        print('The object is too light. It weighs less than 100 newtons.')
        
#   unless, print nothing but weight        
    else:
        print('Object Weight: ', format(object_weight,' .2f'),' newtons', sep='')
        
#   if mass is negative number, print 'you cant do that'
else:
    print('Mass must be >= 0')
