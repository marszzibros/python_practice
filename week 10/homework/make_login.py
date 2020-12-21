#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW09 - 1

#   global constants
LASTNAME_LEN = 7
USERNAME_LEN = 8
BIRTHDAY0_CRITERIA = 10

#   function that generate name
def make_user_name(first_name, last_name, birth_year):
#   replace every word that is not necessary such as ',  - (first_name)
    first_name = first_name.replace('\'','')
    first_name = first_name.replace('-','')
#   change first name into the lower case
    first_name = first_name.lower()

#   replace every word that is not necessary such as ',  - (last_name)
    last_name = last_name.replace('\'','')
    last_name = last_name.replace('-','')
#   change last name into the lower case
    last_name = last_name.lower()

#   refers the userName as empty string
    userName=''
#   if the last_name is less than 7, we have to use more letters in first letter
    if len(last_name) < LASTNAME_LEN:

#   it is fine if total length is less than 8
        if len(first_name) + len(last_name) < USERNAME_LEN:
#   get letters from the first name
            for i in range(0, len(first_name)):
                userName += first_name[i]
#   get letters from the last name
            for i in range(0,len(last_name)):
                userName += last_name[i]

#   but try to make 8 letters from the name
        else:
#   get letters from the first name
            for i in range(0, USERNAME_LEN - len(last_name)):
                userName += first_name[i]
#   get letters from the last name
            for i in range(0,len(last_name)):
                userName += last_name[i]   

#   after generating user name using first and last name, add birth year             
        userName += str(birth_year)        

#   if the length of the lastname is longer or same with 7   
    else:
#   add first letter from the first name
        userName = first_name[0]
#   add 7 letters from the last name
        for i in range(0,LASTNAME_LEN):
             userName += last_name[i]
#   after generating user name using first and last name, add birth year                 
        userName += str(birth_year)              
#   return generated username
    return userName

#   import random variable
import random

#   function for generating password
def make_password(birthday, mytuple):

#   delete '/' seperating birthday.
    birthdayList = birthday.split('/')
#   refers the variable
    password = ''
#   generate random number in order to index the given tuple
    ranIndex = random.randint(1,len(mytuple))
#   if the month is less than 10, add 0 in front of it
#   ex) 1 => 01 
    if int(birthdayList[0]) < BIRTHDAY0_CRITERIA:
        password = password + '0' + birthdayList[0]      
    else:
        password += birthdayList[0]
#   add the random number inside the password
    password += mytuple[ranIndex - 1]

#   if the day is less than 10, add 0 in front of it
#   ex) 1 => 01
    if int(birthdayList[1]) < BIRTHDAY0_CRITERIA:
        password = password + '0' + birthdayList[1]
    else:
        password += birthdayList[1]

#   return password
    return password

#   main function
def main():

#   valid variable to determine if the filename is valid
    valid = False
#   while loop to keep running until the user enter the valid file name
    while valid == False:
#   prompt user to enter the file name
        filename_in = input("What file would you like to read data from?")
        filename_out = input("What file would you like to print data to?")
#   try to open the file
        try:
            readfile = open(filename_in,"r")
            outputfile = open(filename_out,"w")
#   if the file does not exist
        except:
            print("Enter the valid filename")
#   if okay...
        else:
            valid = True
#   refers the tuple for password
            mytuple = ("Otter", "Cow", "Bobcat", "Falcon", "Duck", "Whale", "Owl")
#   make the empty list for inputing employee data
            employee_data = []
#   read the data from the given file
            for value in readfile:
                employee_data.append(value.rstrip('\n').split(','))
#   send and return back from the function above
            for i in range(0,len(employee_data)):
#   get year
                year = int(employee_data[i][2].split('/')[2])
#   print userid and password in the file
                outputfile.write(employee_data[i][0] + ' ' + employee_data[i][1] + '\'s username is: ' + make_user_name(employee_data[i][0], employee_data[i][1], year) + ' password is: ' + make_password(employee_data[i][2], mytuple))
                outputfile.write('\n')
#   close file           
            readfile.close()
            outputfile.close()
main()        
   
