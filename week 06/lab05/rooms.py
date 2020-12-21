#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   LAB05 : room assigning program

#   import random
import random

#   global constant
UNIVERSITY_HEIGHT = 1
MAIN_CAMPUS = 2
ATHLETIC_CAMPUS = 3
TRINITY_CAMPUS = 4

#   main function
def main():

#   call the function 10 times using loop
    for i in range(10):
        selectedDorm = room_draw()
        print(selectedDorm)

#   dorm choosing function function
def room_draw():
#   choose 1 to 4 randomly
    randomDormNum = random.randint(1,4)
#   1 = UH, 2= MC, 3 = AC, 4 = TC     
    if randomDormNum == 1:
        dormRoom = 'University Height'
    elif randomDormNum == 2:
        dormRoom = 'Main Campus'
    elif randomDormNum == 3:
        dormRoom = 'Athletic Campus'
    elif randomDormNum == 4:
        dormRoom = 'Trinity Campus'
#   return the results(string)    
    return dormRoom

#   call main function
main()