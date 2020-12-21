#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   determine if the year is a leap or not

#   input year (int)
print('Welcome too my leap year calculator.')
print('If you give me a year, I can tell you if it is a leap year or not.')
enterYear = int(input('What year? '))

#   leap condition ((year % 4 ==0) and not(year % 100 == 0)) or year % 400 ==0
if ((enterYear % 4 == 0) and not(enterYear % 100 == 0)) or enterYear % 400 == 0:
    print('The year ', enterYear, ' IS a leap year.',sep='')

#   else => it is a common year or faulty results
else :
    print('The year', enterYear, 'is NOT a leap year.',sep='')
