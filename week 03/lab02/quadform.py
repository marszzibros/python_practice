#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   quadratic equation

#   import math module
import math

#   print statements, and imput the three coefficients
print('Rally\'s Quadratic Equation Solver')
print('You\'ll be prompted for the coefficients of the equation ax^2 + bx +c = 0.')
print('The roots will be computed and displayed')
num1 = float(input('a = ? '))
num2 = float(input('b = ? '))
num3 = float(input('c = ? '))

#   using the quadratic equation, find the solution
#   When it is two
if (num2 ** 2) - (4 * num1 * num3) > 0:
    QuadSolution1 = ((- num2) - math.sqrt((num2 ** 2) - (4 * num1 * num3))) / (2 * num1)
    QuadSolution2 = ((- num2) + math.sqrt((num2 ** 2) - (4 * num1 * num3))) / (2 * num1)
    print('The two roots of the equation are ', format(QuadSolution1,'.1f'),' and ', format(QuadSolution2,'.1f'), sep='')
#   When it is one
elif (num2 ** 2) - (4 * num1 * num3) == 0:
    QuadSolution1 = (- num2)/ (2 * num1)
    print('The one root of the equation is ', format(QuadSolution1,'.1f'), sep='')
#  When it is none
else :
    print('there are no real roots to this equation')