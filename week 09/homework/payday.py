#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW 08-01 payday calculator

#   main function
def main():
#   refers variable
    count = 0
    name = []
    workhour = []
    hourRate = []
    total = []
    
#   keep, if an user hits enter, turns to True
    keep = False
    
#   while loop (input until user hit enter)
    while keep == False:
        
#   input name => append in name list
        name.append(input('Name (just hit Enter when done): '))
        
#   if name is not empty => execute
        if name[count] != '':
            
#   try: check if the work hour value is float
            try:                 
                workhour.append(float(input('Hours worked: ')))
                
#   if not => delete the name entered right before and return a print statement
            except ValueError:
                del(name[count])
                print('Value must be numeric.')
                print('Please input employee\'s name and values again.')
                
#   validate value
            else:
#   checking a value that might not cause error, but logically wrong (if the value is negative)
                if workhour[count] <= 0:
                    print('You must enter the number over 0')
#   delete the currently entered value and skip the below
                    del(name[count]) 
                    del(workhour[count])
#   if logically right execute below
                else:
#   try: check if the work hour value is float
                    try: 
                        hourRate.append(float(input('Hourly rate: ')))
#   if not => delete the name entered right before and return a print statement
                    except ValueError:
                        del(name[count]) 
                        del(workhour[count])   
                        print('Value must be numeric')
                        print('Please input employee\'s name and values again.')
#   validate value                       
                    else:
#   checking a value that might not cause error, but logically wrong (if the value is negative)
                        if hourRate[count] <= 0:
                            del(name[count]) 
                            del(workhour[count])
                            del(hourRate[count])      
                            print('You must enter the number over 0')
#   if valid, calculate the final result and add the count
                        else:
                            total.append(float(workhour[count] * hourRate[count]))
                            count += 1
#   if user hits enter
        else:
#   delete '' in the list
            del(name[count])
            keep = True
#   open a writing file
            try:
                openfile = open('payroll.txt','w')

            except IOError:
                print('error occurs!')
            else:
#   print the statements in the file
#   get the final total at the end of the list total (I just append it to use it)
                total.append(0)
                if count != 0:
                    for i in range(count):
                        openfile.write(name[i] + '\t')
                        openfile.write(format(workhour[i],'.2f') + '\t')        
                        openfile.write(format(hourRate[i],'.2f') + '\t')
                        openfile.write(format(total[i],'.2f') + '\t')
                        openfile.write('\n')
                        total[count] += total[i]
                    openfile.write('\n')
#   print total and average
                    openfile.write('Total Payroll = $' + format(total[len(total)-1],'.2f') + '\n')
                    openfile.write('Average Paycheck = $' + format(total[len(total)-1]/count,'.2f'))

#   if no person, it cannot calculate average
                elif count == 0:
                    print('You should have at least one person in your list to calculate average!')
#   file close
                openfile.close()

#   main call
main()
