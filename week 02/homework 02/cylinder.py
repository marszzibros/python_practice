#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   calculate cylinder's surface area & volume

#   constant PI
PI = 3.1415926535

#   input the radius& height of the cylinder
radius = float(input('What is the radius of the base of the cylinder: '))
height = float(input('What is the height of the cylinder: '))


#   calculate& print the results

#   surface area = 2 * (Pi * radius^2) + (Pi * radius * 2) * height
#   print the surface 
surface = ((radius * 2) * height + 2 * radius ** 2) * PI
print('The surface area of the cylinder is:',\
      format(surface,'.2f'))

#   volume = Pi * height * raidus^2
#   print the volume 
volume = PI * height * radius ** 2
print('The volume of the cylinder is:',\
      format(volume, '.2f'))
