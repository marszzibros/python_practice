#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Exercise02: Celsius to Fahrenheit

#   print the table
print('Celsius      Fahrenheit')
print('--------------------------------')

#   using For loop, go to -7 to 36 with +7
for celsius in range(-7,36,7):
#   calculating fahrenheit
    fahrenheit = ((9 / 5) * celsius) + 32

#   print celsius with 4 spaces behind and fahrenheit with 16 spaces behind and two decimals
    print(format(celsius,"4d"),format(fahrenheit,"16.2f"))
