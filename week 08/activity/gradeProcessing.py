# Jackie Horton
# CS21 
# HW 07: grade reading and analyizing program

def main():

    #initialize stats
    low = 100
    high = 0
    total = 0
    try: #try suite
        #open file
        input_file = open('gradesx.txt','r')
    except IOError:
        print('Error opening file')
    else:
        #read data line by line
        try:
            count = 0
            for line in input_file:
                num = int(line)
                count += 1
                if num < low:
                    low = num
                if num > high:
                    high = num
                total += num
        except ValueError:
            print('Invalid data :',line)
        finally:
            #close file
            input_file.close()

            
        try:
            print('There were',count,'grades')
            print('Average:',format(total/count,'.1f'))
        except ZeroDivisionError:
            #do nothing
            print('No average calculated')
        else:
            #display results
            
            print('High grade:', high)
            print('Low grade:', low)
        
main()










