#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Activity 03: arithmetic mean, geometric mean, harmonic mean

#   refer the value inside the variables x, y, z
num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
num3 = int(input("Enter the third value: "))

#   Calculate Arithmetic mean, Geometric mean, and Harmonic mean
#   arit_mean = (x + y + z) / 3
#   geom_mean = (x * y * z) ^ (1 / 3)
#   harm_mean = 3 / ((1 / x) + (1 / y) + (1 / z))

arit_mean = (num1 + num2 + num3) / 3
geom_mean = (num1 * num2 * num3) ** (1 / 3)
harm_mean = 3 / ((1 / num1) + (1 / num2) + (1 / num3))

#   print the calculated means
print('arithmetic mean: ', format(arit_mean, '.2f'))
print('Geometric mean: ', format(geom_mean, '.2f'))
print('Harmonic mean: ', format(harm_mean, '.2f'))