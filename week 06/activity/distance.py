#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup task

#   import math function to get use sqrt
import math

#   main function   
def main():
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    x2 = int(input('Enter x2: '))
    y2 = int(input('Enter y2: '))

#   call the function 'distance'
    print('The distance between the two points is ',format(distance(x1,y1,x2,y2),'.2f'))

#   distance function with two points
def distance(x1,y1,x2,y2):
#   call the sqaure function
    distanceValue = math.sqrt(square(x1,x2) + square(y1,y2))
#   return the calculated value
    return distanceValue

#   square function
def square(num1,num2):
#   return the value of square
    return (num1-num2) ** 2

main()