#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   calculate monthly payment using the given formula

#   variable (int)'principal' input
principal = int(input('How much would you like to borrow? '))

#   variable (float)'apr' input
annual_percentage_rate = float(input('What is the interest rate(APR) of the loan? '))

#   variable (int)'years' input
years = float(input('How many years will it take to pay off the loan? '))

#   calculate& print the results

#   NOTE that the variable 'apr' is a persentage and annual... so (apr / 100)
#   NOTE that the variable 'years' also multiplies with 12 when I calculate... / 12
#   calculate 'monthly_payment = (apr * principal) / (1 - (1 + apr) ** (- years * 12)
monthly_percentage_rate = (annual_percentage_rate / 100) / 12
monthly_payment = (monthly_percentage_rate * principal) / (1 - (1 + monthly_percentage_rate) ** (- years * 12))

#   print montly payments -> print with $sep=''
#   round off to two decimal places
print('The monthly payments are $',format(monthly_payment, '.2f'), sep='')

#   print total payments = montly payments * 12 * years -> print with$sep=''
#   round off to two decimal places
total_payment = monthly_payment * 12 * years
print('The total amount paid is $',format(total_payment, '.2f'), sep='')
