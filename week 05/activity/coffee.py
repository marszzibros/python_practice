#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   coffee calculator

#   Constants 52 weeks = 1 year
YEARWEEK = 52

#   main function
def main():
    price=float(input('Enter cost of coffee: '))
    coffeeNum=int(input('number of coffes per week: '))
    coffee(price,coffeeNum)

#   coffee function
def coffee(price,coffeeNum):
#   calculate days per year
    total_days = coffeeNum * YEARWEEK
#   calculate total price
    totalPrice = total_days * price
#   print the results
    print("Total amount spent on coffee in a year: ", format(totalPrice,'.2f'))

main()