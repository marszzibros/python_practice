#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW06-01 expenses

#   global constants
MPG_CITY = 28
MPG_HWY = 38
GALLON_PRICE = 2.29
YES = 'y'
NO = 'n'
VALID_NUM = 0
PERCENTAGE_MIN = 0
PERCENTAGE_MAX = 100

#   main function
def main():
#   SET YorN as 'y' to enter the while loop
    YorN = YES
    print('Computing your gasoline expenses...')
#   while loop
    while YorN == YES:
#   input total miles
        total_miles = float(input('\nTotal miles driven: '))
#   validity check
        while total_miles < VALID_NUM:
            if total_miles < VALID_NUM:
                total_miles = float(input('Enter a trip value > 0: '))
#   input total miles
        highway_percentage = float(input('Percentage of total miles driven on a highway: '))
#   validity check        
        while not(highway_percentage >= PERCENTAGE_MIN and highway_percentage <= PERCENTAGE_MAX):
            if not(highway_percentage >= PERCENTAGE_MIN and highway_percentage <= PERCENTAGE_MAX):
                highway_percentage = float(input('Enter a percentage between 0 to 100: '))

#   call function, calculating total_gas_consumption
        total_gas_consumption = total_gallons(total_miles, highway_percentage)
#   call function, calculating tripCost
        tripCost = gas_expense(total_gas_consumption)

#   print results
        print('\nHere is the information for your trip: \n')
        print('total miles:',format(total_miles,'.1f'))
        print('Gas consumption:',format(total_gas_consumption,'.1f'),'gal')
        print('Total cost: $', format(tripCost,'.2f'),'\n')

#   check if the user want to calculate again
        YorN = 'a'
        while not(YorN == YES or YorN == NO):
            YorN = input('Compute gas expense for another trip (y or n)? ')
        
#   total_gas_consumption calculating function
def total_gallons(total_miles, highway_percentage):

#   calculate total_highway_miles = total_miles * (highway_percentage / 100)
    total_highway_miles = total_miles * (highway_percentage / 100)

#   calculate total_city_miles = total_miles * (city_percentage / 100)
#   city_percentage = 1 - highway_percentage / 100    
    total_city_miles = total_miles * (1 - highway_percentage / 100)

#   calculate total_gas_consumption using the given statement
    total_gas_consumption = (total_highway_miles / MPG_HWY) + (total_city_miles / MPG_CITY)
    return total_gas_consumption

#   calculate gas cost
def gas_expense(total_gallons):
#   return the calculated cost
    return total_gallons * GALLON_PRICE

#   call main function
main()
