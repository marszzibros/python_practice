#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   calculating average running speed

#   (input)the variables: labs, minutes, seconds
labs = float(input('How many laps did you run? '))
minutes = int(input('For how many minutes did you run? '))
seconds = int(input('For how many seconds did you run? '))

#   miles = labs * 0.25 (miles)
#   total_time(hours) = (minutes * 60 + seconds) / 3600
total_miles = labs * 0.25
total_time = (minutes * 60 + seconds) / 3600

#   (speed)(mph) = (miles) / (time)
speed = total_miles / total_time

#   print the speed that is rounded to one decimal
print('You had an average speed of ', format(speed, '.1f'), ' mph!', sep='')
