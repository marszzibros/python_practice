#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup exercise

#   weight is float type, input
#   height is int type, input
my_name = input("Enter your name: ")
my_height = int(input("Enter your height in centimeters: "))
my_weight = float(input("Enter your weight in Kilograms: "))

#   BMI = weight / ((0.01 * height) ^ 2)
bmi = my_weight / (0.01 * my_height) ** 2
print(my_name + ', your BMI is ', format(bmi,'.1f'), sep='')