#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW04-02: Creating monthly payment chart for a loan

cumulative_int = 0.0
#   variable (int)'loan_amount' input
loan_amount = int(input('Original loan amount? '))

#   variable (float)'apr' input
annual_percentage_rate = float(input('Annual interest rate? '))

#   variable (int)'years' input
years = int(input('Years? '))

#   validity test
while loan_amount <=  0 or annual_percentage_rate <= 0 or years <= 0:
    print('You enter the wrong number, please enter again')
    loan_amount = int(input('Original loan amount? '))
    annual_percentage_rate = float(input('Annual interest rate? '))
    years = int(input('Years? '))

#    change to month
total_month = years * 12

#   NOTE that the variable 'apr' is a persentage and annual... so (apr / 100)
#   NOTE that the variable 'years' also multiplies with 12 when I calculate... / 12
#   calculate 'monthly_payment = (apr * loan_amount) / (1 - (1 + apr) ** (- years * 12)
monthly_percentage_rate = (annual_percentage_rate / 100) / 12
monthly_payment = (monthly_percentage_rate * loan_amount) / (1 - (1 + monthly_percentage_rate) ** (- years * 12))

#   Print montly payments -> print with $sep=''
#   Round off to two decimal places
print('Payment is $ ',format(monthly_payment,'.2f'), sep='')

print('Month', 'Interest', 'Cumulative', 'Principal', sep='     ')
print('    ', 'this month', 'Interest', sep='     ')

for i in range(1, total_month+1):
#   monthly_interest calculation
    thisMonth = loan_amount * monthly_percentage_rate
    
#   cumulative interest
    cumulative_int += thisMonth
    
#   monthly payment - this month interest
#   I do not want to use round function but if not, I cannot code correctly as instruction mentions...
    deduction = round(monthly_payment,2) - thisMonth
    
#   principal
    loan_amount -= deduction
    
#   print interest this month, cumulative interest, principal
    print(format(i, '3d'), end='')
    print(format(thisMonth, '14.2f'),format(cumulative_int, '14.2f'), format(loan_amount, '14.2f'))



