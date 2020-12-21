#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   sphere.py

#   Constants PI
PI = 3.1415926535 
#   main function
def main():
    radius = float(input('Enter the radius: '))
    sphere(radius)

#   sphere function
def sphere(radius):
#   Area calculation
    speareArea = 4 * PI * radius ** 2
#   Volume calculation
    speareVol = (4 / 3) * PI * radius ** 3
    print("Area:", format(speareArea,'.2f'))
    print("Volume:", format(speareVol,'.2f'))

main()
