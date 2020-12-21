#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Exercise04: pattern

#   Enter the number of the stars that users want to draw
numStar = int(input('How many stars would you want to draw? '))

#   draw stars
for i in range(numStar,0,-1):
    for j in range(0,i):
        print('*',end='')
    print('\n')


#   for i in range(1,8):
#       for j in range(1,i+1):
#            print('*',end='')
#        print('\n')
#
#   *
#   **
#   ***
#   ****
#   *****
#   ******
#   *******

#   for i in range(1,8):
#       for j in range(7,i,-1):
#            print(' ',end='')
#       for j in range(1,i+1):
#            print('*',end='')
#        print('\n')
#
#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******