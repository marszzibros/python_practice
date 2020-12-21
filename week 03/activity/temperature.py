#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warm up exercise (determine whether it is extreme and normal)

#   input temperature
temperature = int(input('Enter temperature: '))

#   if condition (60 <= temperature <= 80) print normal
if temperature >= 60 and temperature <= 80:
    print('normal')

#   unless, print extreme    
else:
    print('extreme')    