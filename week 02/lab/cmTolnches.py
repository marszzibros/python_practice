#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   changing unit(centimeters to inches)

#   (input)Enter the length in centimeters
centimeters = float(input('What is the length in centimeters? '))

#   change centimeters to inches, inches = 2.54 / centimeters 
inches = centimeters / 2.54

#   print the inches which are rounded to two decimal places
print('\n',format(centimeters,'.2f'), 
' centimeters is ', format(inches, '.2f'), ' inches!', sep='')

