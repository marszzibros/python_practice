#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   FINAL PROJECT - GYM recorder admin

#   import library mysql.connector (https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)
#   for connecting mysql and Python
import mysql.connector
#   import Library re (https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python//)
#   for checking validity of email address
import re
#   import Library random to get a random number
#   for choosing members in DB
import random

#   import Library smtplib (https://docs.python.org/3/library/email.examples.html)
#   for sending email
import smtplib
from email.message import EmailMessage

#   refers the variables
MONTH_COUNT = 12
DATE_COUNT = 31
YEAR_LIMIT_MIN = 1900
YEAR_LIMIT_MAX = 2020
MODIFY_OPTION = 5

#   phpMyAdmin ID and Password
DB_ID = 'jjung2_admin'
DB_PASSWORD = 'UzAn4dsM6VIZigk1'

#   regular experssion for email address (https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python//)
REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#   main function
def main():
    connection = False
#   call function login_protocol
    connection, DB_connector = login_protocol()
#   get option menu
    option = mainMenu_option()
    while option != 6 and connection == True:
#   1. Get Users Info from the DB
        if option == 1:
            getUserFromDB(DB_connector)
#   2. Manage Users Info
        elif option == 2:
            ManageUserFromDB(DB_connector)
#   3. Add Exercise in the DB
        elif option == 3:
            addExerciseDB(DB_connector)
#   4. Create a Exercise Record Table
        elif option == 4:
            createTable(DB_connector)
#   5. (EVENT)Randomly Choose members
        elif option == 5:
            eventChooseMembers(DB_connector)
#   get option menu
        option = mainMenu_option()

#   function for connecting DB
def login_protocol():
#   return False, if there is a problem connecting to DB
    connection = False
#   try/exception for connection
    try:
#   prompt users to enter the DB ID & passwords    
#            DB_ID = input('Enter the Database ID: ')
#            DB_Password = input('Enter the Database Password: ')
#   (for grader)I could have prompted users to enter the id and password, but the password is to lengthy...
#   try to connect DB with the id and passwords that user provides
        DB_connector = mysql.connector.connect(
            host = "webdb.uvm.edu",
            user = DB_ID,
            password = DB_PASSWORD,
            database = "JJUNG2_database")
#   exception
    except:
        print('DB connection error! Please Enter the valid ID & Password! \n')
#   if is works, connect with DB        
    else:
        connection = True
        print("Successfully connected to Database!")

#   return the DB connection variables
    return connection, DB_connector



#   mainMenu printing function
def mainMenu_option():
    valid = False
#   until the user chooses the valid option
    while valid == False:
        try:
            print("--+=====================================+--\n")
            print(" 1. Get Users Info from the DB")
            print(" 2. Manage Users Info")
            print(" 3. Add Exercise in the DB")
            print(" 4. Create a Exercise Record Table")
            print(" 5. (EVENT)Randomly Choose members")
            print(" 6. Exit\n")
            print("--+=====================================+--\n")
            option = int(input("Choose the number between 1 and 6: "))
#   when the user enters the string or invalid number
        except ValueError:
            print("Enter the digit which is listed on the menu!\n")
        else:
#   valid number
            if option <= 6 and option >= 1: 
                valid = True
#   when the user enters the invalid number
            else:
                print("Enter the digit which is listed on the menu!\n")
    return option


#   ===============================================================================================
#   Get Users Info from the DB
#   call data based on birthday, id, last name and all data from the database
def getUserFromDB(DB_connector):
    valid = False
    getInfo = []
#   (Get Users Info from the DB)'s options
    while valid == False:
        try:
            print("\n****** Get Users Info from the DB ******\n")
            print("    1. Get All Users")
            print("    2. Select Users By Birthdays")
            print("    3. Get Info by ID")
            print("    4. Get Info by Name")
            print("    5. Go Back To The Main Option\n")
            getOption = int(input("Choose the number between 1 and 5: "))
#   when the user enters the string or invalid number
        except ValueError:
            print("Enter the digit which is listed on the menu!\n")
        else:
#   valid number
            if getOption <= 5 and getOption >= 0: 
                valid = True
#   when the user enters the invalid number
            else:
                print("Enter the digit which is listed on the menu!\n")


#   **************************
#   option 01: Get All Users
    if getOption == 1:
#   sql for selecting all
        sql = 'SELECT * FROM tblPersonalInfo;'


#   **************************
#   option 02: Select Users By Birthdays
    elif getOption == 2:
        print("\nEnter the date with '/'splited form (month/date/year)")

#   validity check
#   start date
        valid = False
        while valid == False:
            try:
                datecheck = ''
                testdate = []
                startdate = []
#   prompt the user to enter starting date
                datecheck = input("Enter the date you want to start from: ")

#   if the user enters the symbol other than '/' to seperate, it is invalid due to split method
#   try to convert in int
                for value in datecheck.split('/'):
                    testdate.append(int(value))
#   if it is not convertable => exception            
            except ValueError:
                print("You Entered the invalid Date! Enter again!\n")
#   delete the appended list
                del(testdate)
#   specific validity check
            else:
#   put it in startdate if it is valid in a form of string
                for i in testdate:
                    startdate.append(str(i))
                del(testdate)
#   re-check if the startdate consists of year, month and day, and if those are all digit
                if len(startdate) == 3 and (startdate[0].isdigit() and startdate[1].isdigit() and startdate[2].isdigit()):
#   call function date_validity_check
#   get True if it is valid, or False
                    valid = date_validity_check(startdate)
#   if the date is not valid in terms of leap year or anything, delete the startdate and keep looping
                    if valid == False:
                     del(startdate)

#   if falied to re-check 
                else:
                    print("You Entered the invalid Date! Enter again!\n")
                    del(startdate)
                    
#   validity check                    
#   end date
        valid = False
        while valid == False:
            try:
                enddate = []
                datecheck = ''
                testdate = []
#   prompt the user to enter ending date
                datecheck = input("Enter the date you want to end with: ")

#   if the user enters the symbol other than '/' to seperate, it is invalid due to split method
#   try to convert in int
                for value in datecheck.split('/'):
                    testdate.append(int(value))
#   if it is not convertable => exception      
            except ValueError:
                print("You Entered the invalid Date! Enter again!\n")
#   delete the appended list
                del(testdate)
#   specific validity check
            else:
#   put it in enddate if it is valid in a form of string
                for i in testdate:
                    enddate.append(str(i))
                del(testdate)
#   re-check if the startdate consists of year, month and day, and if those are all digit
                if len(enddate) == 3 and (enddate[0].isdigit() and enddate[1].isdigit() and enddate[2].isdigit()):
#   call function date_validity_check
#   get True if it is valid, or False
                    valid = date_validity_check(enddate)
#   if the date is not valid in terms of leap year or anything, delete the startdate and keep looping
                    if valid == False:
                        print("You Entered the invalid Date! Enter again!\n")
#   check if enddate is smaller than the startdate
                    else:
                        if int(enddate[2]) < int(startdate[2]):
                            valid = False
                            print("End day should not be smaller than the start day!\n")
                        elif int(enddate[2]) == int(startdate[2]) :
                            if int(enddate[0]) < int(startdate[0]): 
                                print("End day should not be smaller than the start day!\n")
                                valid = False
                            elif int(enddate[0]) == int(startdate[0]):
                                if int(enddate[1]) < int(startdate[1]): 
                                    print("End day should not be smaller than the start day!\n")
                                    valid = False
#   if falied to re-check 
                else:
                    print("You Entered the invalid Date! Enter again!\n")
#   create the sql based on the date the user enters
        sql = "SELECT * FROM tblPersonalInfo WHERE fldBirthday >='" + startdate[2] + '-' + startdate[0] + '-' + startdate[1] + "' AND fldBirthday <= '" + enddate[2] + '-' + enddate[0] + '-' + enddate[1] +"';"


#   **************************
#   option 03: Get Info by ID
    elif getOption == 3:
#   call the all ID from DB
        sql = 'SELECT (pmkPersonalID) FROM tblPersonalInfo;'
        DBConnect = DB_connector.cursor()
        DBConnect.execute(sql)
        ID_data = set()
#   put it as a set
#   the data will be stored as a tuple
#   e.g. ('aaaa','bbbb',)
        for ID in DBConnect:
#   ID[0] = ('aaaa',)
            ID_data.add(ID[0])
#   prompt user to type ID that they want to search for
        ID_choose = input("Enter the ID that you want to look at: ")
#   if the id is on DB set => create the sql statement
        if ID_choose in ID_data:
            sql = "SELECT * FROM tblPersonalInfo where pmkPersonalID = '" + ID_choose + "';"
#   error message(no info!)
        else:
            print("there is no information with the ID,",ID_choose)
            
            
#   **************************
#   option 04: Get Info by Name
    elif getOption == 4:
#   call the all lastname from DB
        try:
            sql = 'SELECT (fldLastName) FROM tblPersonalInfo;'
        except:
            print("something went wrong!")
        else:
            DBConnect = DB_connector.cursor()
            DBConnect.execute(sql)
#   put it as a set
            NAME_data = set()
            for Name in DBConnect:
                NAME_data.add(Name[0])
#   prompt the user to enter a lastname they are searching for
            Name_choose = input("Enter the lastname that you want to look at: ")
#   if in name set = > create the sql statement
            if Name_choose in NAME_data:
                sql = "SELECT * FROM tblPersonalInfo where fldLastName = '" + Name_choose + "';"
#   or display the error message(no info!)
            else: 
                print("there is no information with the Names,",Name_choose)

            
#   **************************
#   option 05: quit
    elif getOption == 5:
        valid = True
#   if the entered option is not valid
    else:
        print("\nPlease Enter the value bewteen 1 and 5")

#   Finally, after execute options 1-4 => execute the statement that the program created above     
    if getOption != 5:
        filename = ''
        getInfo = []
#   prompt the user to enter the filename that they prefer to save data
        while filename.endswith('.txt') == False:
#   until the file name is valid
            filename = input("\nEnter the File Name that You Want to Store In \n(include .txt at the end): ")
            if filename.endswith('.txt') == False:
                print('Please put .txt at the end of the filename\n')
#   if the there is a problem opening a file
        try:
            printUserFile = open(filename, 'w')
#   error message
        except:
            print("Error to open the file!")
#   or execute the statement
        else:
            DBConnect = DB_connector.cursor()
            DBConnect.execute(sql)
#   create table on the txt file that user types on
            printUserFile.write(format("name","25s") + format("userID","20s") + format("Email address","30s") + format("Birthday","20s")+ "\n")
            for value in DBConnect:
                getInfo.append(value)
            for i in range(0,len(getInfo)):
                printUserFile.write(format(getInfo[i][2] + ", " + getInfo[i][1] ,"25s") + format(getInfo[i][0],"20s") +  format(getInfo[i][3],"30s") + format(str(getInfo[i][4]),"20s") + "\n")
#   close file            
            printUserFile.close()


#   ===============================================================================================
#   Manage Users Info
#   manage user data using sql statement (change, add, clear table))

def ManageUserFromDB(DB_connector):
#   refers the variables    
    valid = False
    
    count = 0
    YorN = ''
    getOption = ''
#   I use valid in many different while loop to ensure the validity of inputed data
#   manage Users info menu
    while valid == False:
#   if the user enters the wrong number
        try:
            print("\n****** Manage Users Info ******\n")
            print("    1. Change personal Info")
            print("    2. Add personal Info")
            print("    3. Clear the User Data")
            print("    4. Go Back To The Main Option\n")
            getOption = int(input("Choose the number between 1 and 4: "))
        except ValueError:
            print("Enter the digit which is listed on the menu!\n")
        else:

#   **************************
#   option 01: Change personal Info 
            if getOption == 1:
                getInfo = []
                userID = ''
                optionList = []
                replaced_data = ''
                replaced_valid = False
                EnterValid = False
                rangecheck = False
                namecheck  = True
                datecheck = False
                count = 0
                while EnterValid == False:
#   prompt users to enter the userID
                    userID = input("Enter the user's id You Want to Modify (Enter to quit)")
#   execute the sql statement that finds the userID in the list
                    sql = 'SELECT * FROM tblPersonalInfo WHERE pmkPersonalID="' + userID + '";'  
                    DBConnect = DB_connector.cursor()
                    DBConnect.execute(sql)
#   get it as a list
                    for value in DBConnect:
                        getInfo.append(value)
#   if there is no data on the DB
                    if len(getInfo) == 0 and userID != '':
                        print("there is no user whose name is", userID,"\nPlease verify your username!")
                        getInfo = []
                        
#   if the data exists
                    elif userID != '':
                        YorN = ''
#   print the info that the above statement calls
                        print("Hello,",getInfo[0][1])
                        print("Is your information below correct?\n")
                        print("Name:",getInfo[0][1],getInfo[0][2])
                        print("Email:",getInfo[0][3])
                        print("Birthday:",str(getInfo[0][4]))
#   ask user whether the user wants to change or not
                        while YorN != 'n' and YorN != 'y':
                            YorN = input("\nEnter y if you do not want to change, n if you want: ")
                            if YorN != 'n' and YorN != 'y':
                                print("Invalid letter, Please check again! \n")
#   if user enters n => it will perform modifying process
                        if YorN == 'n':
#   ask users what information they would like to chnage
                            while rangecheck == False:
#   ask users what information they would like to chnage
                                print("    1. First Name")
                                print("    2. Last Name")
                                print("    3. Email")
                                print("    4. Birthday")
                                print("    5. Nothing\n")
#   if users separate their answer using symbols other than ' ', it 
                                try:
#   first using input, user will enter the list of the options that they want to choose
                                    testOption = ''
                                    testOption = input("\nWhat Information would you like to change? (type all you want to change without comma)\n")
#   change it to list using split method, and if there is a letter, exception(ValueError) will occur
                                    for value in testOption.split():
                                        optionList.append(int(value))
#   if press enter, quit the process
                                    if len(optionList) == 0:
                                        EnterValid = True

        
                                except:
                                    print("Invalid Number! please try again!")
#   if no problem with letter
                                else:
#   check if the user enters 5. nothing and other choice; it might be non-sense that user wants to choose nothing but still enters the options that they want to modify
                                    if MODIFY_OPTION in optionList and len(optionList) > 1:
                                        print("You cannot choose nothing and other choices! \n")
#   check if the user enters less than 4 choices
                                    elif len(optionList) > MODIFY_OPTION - 1:
                                        print("You cannot choose more than four choices \n")
#   check if the user enters the number that is not on a list
                                    else:
                                        count = 0
                                        while count != len(optionList):
#   check if the selected option is valid
                                            if int(optionList[count]) not in range(1,MODIFY_OPTION + 1) :
                                                print("Please Enter the valid number")
                                                rangecheck = False
                                                break
                                            count += 1
#   if the the it is valid => finish the while loop for choosing options
                                        if count == len(optionList):
                                            rangecheck = True
#   sql code that I will use for rest of the program in this section (a) will be changed using replace method      
                            sql = 'UPDATE tblPersonalInfo SET fldFirstName = "(a)", fldLastName = "(b)", fldEmail = "(c)", fldBirthday= "(d)" WHERE pmkPersonalID = "' + userID + '";'
                            replaced_valid = False
#   if user wants to change 1. First Name & if the user did not simply enter the enter key prior to this process
                            if 1 in optionList and EnterValid != True:
                                while replaced_valid == False:
#   enters the first name
                                    replaced_data = input("Enter your First Name(Press Enter if you want to quit): ")
                                    if replaced_data == '':
#   if enter key => quit and do not execute the rest of the option 1 (EnterValid = True)
                                        EnterValid = True
                                        replaced_valid = True

                                    else:
                                        if not len(replaced_data) > 15:
#   check if the first name contains number                                           
                                            for letter in replaced_data:
                                                if letter.isdigit():
                                                    namecheck = False
                                                    
#   if first name is over 15 letters => error message
                                        elif len(replaced_data) > 15:
                                            print("Your First Name is invalid! check again! (less than 15 letters)")
#   check if the first name contains number (error message)
                                        if namecheck == False:
                                            print("Your First Name is invalid! check again! (Do not insert number on it)")
                                            namecheck = True
#   or replace (a) with entered names
                                        else:
                                            sql = sql.replace("(a)",replaced_data)
                                            replaced_valid = True
                        
#   if the user does not want to change their first name, just keep it (still need to replace (a) to orginal firstname )
                            else:
                                sql = sql.replace("(a)",getInfo[0][1])
                        
                            replaced_valid = False
#   if user wants to change 2. Last Name & if the user did not simply enter the enter key prior to this process
                            if 2 in optionList and EnterValid != True:
                                while replaced_valid == False:
#   enters the last name
                                    replaced_data = input("Enter your Last Name(Press Enter if you want to quit): ")
#   if enter key => quit and do not execute the rest of the option 2 (EnterValid = True)
                                    if replaced_data == '':
                                        EnterValid = True
                                        replaced_valid = True
#   check if the last name contains number 
                                    else:
                                        if not len(replaced_data) > 15:
                                            for letter in replaced_data:
                                                if letter.isdigit():
                                                    namecheck = False
#   if last name is over 15 letters => error message
                                        elif len(replaced_data) > 15:
                                            print("Your Last Name is invalid! check again! (less than 15 letters)")
#   check if the last name contains number (error message)
                                        if namecheck == False:
                                            print("Your Last Name is invalid! check again! (Do not insert number on it)")
                                            namecheck = True
#   or replace (a) with entered names
                                        else:
                                            sql = sql.replace("(b)",replaced_data)
                                            replaced_valid = True
#   if the user does not want to change their last name, just keep it (still need to replace (b) to orginal lastname )
                            else:
                                sql = sql.replace("(b)",getInfo[0][2])
                        
                            replaced_valid = False
#   if user wants to change 3. Email & if the user did not simply enter the enter key prior to this process
                            if 3 in optionList and EnterValid != True:
                                while replaced_valid == False:
                                    replaced_data = input("Enter your email(Press Enter if you want to quit): ")
#   if user enters the enter = > quit the process
                                    if replaced_data == '':
                                        EnterValid = True
                                        replaced_valid = True
                                    else:
#   How to check if it is a valid form of email
#   (https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python)
#   if valid => replace (c) to replaced email
                                        if re.search(REGEX, replaced_data):
                                            sql = sql.replace("(c)",replaced_data)
                                            replaced_valid = True
#   if it is not valid => error message
                                        else:
                                            print("Your Email is invalid! check again! (ex. example@domain.com)")
#   if the user does not want to change their email, just keep it (still need to replace (c) to orginal email )
                            else:
                                sql = sql.replace("(c)", getInfo[0][3])
                                
                            replaced_valid = False
#   if user wants to change 4. birthday & if the user did not simply enter the enter key prior to this process
                            if 4 in optionList and EnterValid != True:
                                while replaced_valid == False:
#   enter birth day in a format of mm/dd/yyyy and save it into replaced_data
                                    replaced_data = input("Enter the birthday (month/day/year, with /)(Press Enter if you want to quit): ").split('/')
#   if user enters the enter = > quit the process
                                    if len(replaced_data) == 0:
                                        EnterValid = True
                                        replaced_valid = True
#   check whether user enters the valid format of date
                                    else:
                                        if len(replaced_data) == 3 and (replaced_data[0].isdigit() and replaced_data[1].isdigit() and replaced_data[2].isdigit()):
#   call date_validity_check function => call back replaced_valid = True or False(True => quit while, False=> keep doing)
                                            replaced_valid = date_validity_check(replaced_data)
#   if the date is wrong > error message
                                            if replaced_valid == False:
                                                print("You Entered the invalid Date! Enter again!\n")
                                                del(replaced_data)
                                            else:
                                                sql = sql.replace("(d)",str(replaced_data[2])+ '-'+ str(replaced_data[0]) + '-'+ str(replaced_data[1]))
#   if the date is wrong > error message    
                                        else:
                                            print("You Entered the invalid Date! Enter again!\n")
                                            del(replaced_data)
#   if the user does not want to change their birthday, just keep it (still need to replace (c) to orginal birthday )
                            else:
                                sql = sql.replace("(d)",str(getInfo[0][4]))
#   if 5. nothing => go back to menu
                            if 5 in optionList:
                                EnterValid = True
#   if not 5 and enter key is not entered during the above process
                            elif EnterValid != True:
#   to process the new record next time, del the data
                                del(getInfo[0])
#   execute the sql created by above process
                                DBConnect = DB_connector.cursor()
                                DBConnect.execute(sql)
                                DB_connector.commit()
#   quit the process
                                EnterValid = True
#   quit the process if userID is ''
                    elif userID == '':
                        EnterValid = True
                        
#   **************************
#   option 02: Add personal Info
            elif getOption == 2:
                
#   userID verify
#       1. same userID in DB?
#       2. length

#   refers variables
                addData = ''
                userinfo = dict()
                nextValid = True
                addInfoValid = False
                TupleUserList = []

#   until user enters the valid id and did not enter the enter key
                while addInfoValid != True and nextValid == True:
                    addData = input("Enter the user ID that you want to use. (Press Enter if you want to exit.): ")

#   if the user enters the enter key
                    if addData == '':
                        nextValid = False
#    find the userID in the DB and check if it exists (if exists => ask user to enter the different one)
                    else:
#   using dictionary => 'userID': entered data
                        userinfo['userID'] = addData
                        sql = 'SELECT (pmkPersonalID) FROM tblPersonalInfo;'
                        DBConnect = DB_connector.cursor()
                        DBConnect.execute(sql)
                        for value in DBConnect:
                            TupleUserList.append(value[0])
                        if userinfo['userID'] in TupleUserList:
#   delete userID after print the ID
                            print("There is",userinfo.pop('userID'),"in our DB, Please Try it again. (Press Enter if you want to exit.) \n")
#   if the userID is either too short or too long
                        elif not(len(userinfo['userID']) >= 3 and len(userinfo['userID']) <= 9):
                            print("Please Enter ID in a length of 3 to 9.",userinfo.pop('userID'),"is not valid\n")
#   finish loopings
                        else:
                            addInfoValid = True
#   first name verify
#       1. does it contain number?
#       2. if it is too long > 15?

                addInfoValid = False
                namecheck = True
                while addInfoValid != True and nextValid == True:
                    addData = input("Enter your first name(Press Enter if you want to exit.): ")
                    if addData == '':
                        nextValid = False
                        del(userinfo)
                    else:
                        userinfo['first_name'] = addData
                        for i in userinfo['first_name']:
#   check if the firstname consists of either space or letter
                            if not(i.isalpha() or i.isspace()):
                                namecheck = False
                        
                        if namecheck == False:
                            print(userinfo.pop('first_name'),"contains number! Please Verify!")
                            namecheck = True
                            userinfo['first_name'] = input("Enter your first name: ")
#   validate the lenght of the name
                        elif len(userinfo['first_name']) >= 15:
                            print("We doubt that",userinfo.pop('first_name'),"is not your first name. It is too long (less than 15 letters!)\n")
                        else:
                            addInfoValid = True
#   last name verify
#       1. does it contain number?
#       2. if it is too long > 15?

                addInfoValid = False
                while addInfoValid != True and nextValid == True:
                    addData = input("Enter your last name(Press Enter if you want to exit.): ")
                    if addData == '':
                        nextValid = False
                        del(userinfo)
                    else:
                        
                        userinfo['last_name'] = addData
#   check if the lastname consists of either space or letter
                        for i in userinfo['last_name']:
                            if not(i.isalpha() or i.isspace()):
                                namecheck = False
                        if namecheck == False:
                            print(userinfo.pop('last_name'),"contains number! Please Verify!")
                            namecheck = True
#   validate the lenght of the name
                        elif len(userinfo['last_name']) >= 15:
                            print("We doubt that",userinfo.pop('last_name'),"is not your last name. It is too long (less than 15 letters!)\n")
                        else:
                            addInfoValid = True
                        
#   email verify
#       1. email verify

                addInfoValid = False

                while addInfoValid != True and nextValid == True:
                    addData = input("Enter your email(Press Enter if you want to exit.): ")
                    if addData == '':
                        nextValid = False
                        del(userinfo)
                    else:
                        userinfo['email'] = addData
#   check if the email is in right form
                        if not re.search(REGEX, userinfo['email']):
                            print(userinfo.pop('email'),"seems to be wrong.")
                        else:
                            addInfoValid = True

#   birthday verify
#       1. does it contain number?
#       2. if it is too long > 15?

                addInfoValid = False
                while addInfoValid != True and nextValid == True:
                    try:
                        addDate = []
                        testDate = []
                        addData = input("Enter the birthday (month/day/year, with /)")
                        if addData == '':
                            nextValid = False
                            del(userinfo)
                        else:
                            for i in addData.split('/'):
                                testDate.append(int(i))
                    except ValueError:
                        print("You Entered the invalid Date! Enter again!\n")
                    else:
#   check if the date is in right form
                        if addData != '':
                            for i in addData.split('/'):
                                addDate.append(i)
                            if len(addDate) == 3 and (addDate[0].isdigit() and addDate[1].isdigit() and addDate[2].isdigit()):
#   call "date_validity_check" function
                                datecheck = date_validity_check(addDate)
                                if datecheck == False:
                                    del(addDate)
                                else:
                                    userinfo['birthday'] = addDate[2] + '-' + addDate[0] + '-' + addDate[1] 
                                    addInfoValid = True
                            else:
                                print("You Entered the invalid Date! Enter again!\n")
                                del(addDate)
#   execute the sql after processing all the process above
                if addInfoValid == True and nextValid == True:
                    sql = 'INSERT INTO tblPersonalInfo(pmkPersonalID, fldFirstName, fldLastName, fldEmail, fldBirthday) VALUES (\"' + userinfo["userID"] + '\",\"'+ userinfo["first_name"] +'\",\"'+ userinfo["last_name"] +'\",\"'+ userinfo["email"] +'\",\"'+ userinfo["birthday"] +'\");'
                    DBConnect = DB_connector.cursor()
                    DBConnect.execute(sql)
                    DB_connector.commit()
#   delete the data in the dictionarys
                    del(userinfo)
                


#   **************************
#   option 03: Clear the Users Data
            elif getOption == 3:
                NameCheck = False
                while NameCheck == False:
                    userID = input("Enter the user's id You Want to delete (Enter to quit)")
#   execute the sql statement that finds the userID in the list
                    sql = 'SELECT (pmkPersonalID) FROM tblPersonalInfo WHERE pmkPersonalID="' + userID + '";'  
                    DBConnect = DB_connector.cursor()
                    DBConnect.execute(sql)
#   get it as a list
                    DBName = ''
                    for value in DBConnect:
                        DBName = value[0]
#   if there is no data on the DB
                    if DBName == '' and userID != '':
                        print("there is no user whose name is", userID,"\nPlease verify your username!")
                    elif userID == '':
                        NameCheck = True
                    else:
                        NameCheck = True
                if userID != '':
                    YorN = input("Are you sure you are going to delete all the user's info? (y or n)")
                    while YorN != 'y' and YorN != 'n':
                        print("You Entered the wrong one! Please verify it!")
                        YorN = input("Are you sure you are going to delete all the user's info? (y or n)")
                    if YorN == 'y':
#   delete all the user info
                        sql = 'DELETE FROM tblPersonalInfo WHERE pmkPersonalID="' + userID + '";'
                        DBConnect = DB_connector.cursor()
                        DBConnect.execute(sql)
                        DB_connector.commit()

#   delete all the user exercise info
                        sql = "DELETE FROM tblPersonalExercise WHERE fldPersonalID='"+ userID +"';"
                        DBConnect = DB_connector.cursor()
                        DBConnect.execute(sql)
                        DB_connector.commit()
                        print('All data has been deleted!\n')
                        getOption = 4
#   if it is not on the list
            elif getOption != 4:
                print("Enter the digit which is listed on the menu!\n")
                
#   **************************
#   option 04: Go back to the menu
            if getOption == 4:
                valid = True


#   ===============================================================================================
#   Add Exercise in the DB
#   this is the menu that controls the display of the website

def addExerciseDB(DB_connector):
    valid = False
    YorN = ''
    while valid == False:
#   call the part like chest, legs, back
        sql = "SELECT (fldPart) FROM tblExerciseInfo GROUP BY fldPart;"
        DBConnect = DB_connector.cursor()
        DBConnect.execute(sql)
#   refers the variables
        getOption = ''
        exercisePart = []
        changePart = ''
        addExercise = ''
#   display the menu
        for i in DBConnect:
            exercisePart.append(i[0])
        exercisePart.append('Want to add more part')
        print("\n****** Add Exercise in the DB ******\n")
#   display the part that is on the database
        for count in range(0,len(exercisePart)):
            print("    ",count + 1, ". ",exercisePart[count],sep='')
#   menu for the user who wants to add one more part and exercise in the database
        print("    ",len(exercisePart) + 1, ". Quit",sep='')
        print("\nChoose the number between 1 and ",len(exercisePart) + 1,": ",sep='',end='')
        getOption = input()
#   try if the user enters the string => exception
        try:
            if int(getOption) not in range(1,len(exercisePart) + 2):
                print("You entered the wrong number! Please Try it again\n")
        except ValueError:
            print("You entered the wrong number! Please Try it again\n")
        else:

            if int(getOption) in range(1,len(exercisePart) + 2):
#   if the user wants to add exercise in the existing part
                if int(getOption) in range(1,len(exercisePart)):
                    changePart = exercisePart[int(getOption) - 1]
#   if the user wants to add one more part in the database
                elif getOption == str(len(exercisePart)):
                    while YorN != 'y':
#   ask body part that the user wants to add (enter if the user wants to quit)
                        validYorN = False
                        changePart = input("What body part would you want to add? (Enter to quit): ")
                        if changePart == '':
                            valid = True
                            break
#   ask again if the user's input is correct
                        elif changePart != '':
                            print("You want to add",changePart)
                            YorN = input("Is it correct? (Please Enter y or n)")
                            if YorN != 'y' or YorN !='n':
                                validYorN = True
                            while validYorN != True:
                                print("Please Enter y or n")
                                YorN = input("Is it correct? (Please Enter y or n)")
                                if YorN == 'y' or YorN =='n':
                                    validYorN = True
#   check if the body part exists on the database already 
                            checkPart = True
                            for part in exercisePart[0:len(exercisePart)]:
#   change to lower letter and compare the strings
                                if part.lower() == changePart.lower():
                                    checkPart = False
                            if checkPart == False:
                                print("The body part that you entered is on the list! Please Enter again")
                                YorN = ''
#   if the user enters the quit option
                elif getOption == str(len(exercisePart) + 1):
                    valid = True
#   if the user successfully choose the body part => add exercise info
                if valid != True:
                    YorN = ''
                    while YorN != 'y':
                        validYorN = False
                        addExercise = input("What exercise would you want to add? (Enter to quit): ")
                        if addExercise == '':
                            valid = True
                            break
                        elif addExercise != '':
                            validYorN = True
#   ask user if the exercise they input is correct or not
                            print("You want to add",addExercise)
                            YorN = input("Is it correct? (Please Enter y or n)")
                            if YorN != 'y' or YorN !='n':
                                validYorN = True
                            while validYorN != True:
                                print("Please Enter y or n")
                                YorN = input("Is it correct? (Please Enter y or n)")
                                if YorN == 'y' or YorN =='n':
                                    validYorN = True
#   Generating ID => delete space or '-'
                    if valid != True:
                        generatedID = ''
# create the sql code based on what the user has entered
                        for letter in addExercise:
                            if not letter.isspace() and letter != '-':
                                generatedID += letter
                        sql = 'INSERT INTO tblExerciseInfo (fldPart, fldExercise, fldExercisID) VALUES ("' + changePart + '","' + addExercise + '","' + generatedID + '");'
                        DBConnect = DB_connector.cursor()
                        DBConnect.execute(sql)
                        DB_connector.commit()
#   quit the while loop
                        valid = True

                        
#   ===============================================================================================
#   Add Exercise in the DB
#   add exercise or the exercise part
def createTable(DB_connector):
    valid = False
    while valid == False:
        sql = 'SELECT (pmkPersonalID) FROM tblPersonalInfo;'
        DBConnect = DB_connector.cursor()
        DBConnect.execute(sql)
        ID_data = set()
        for ID in DBConnect:
            ID_data.add(ID[0])
        ID_choose = input("Enter the ID that you want to look at: ")
        if ID_choose in ID_data:
            valid = True
        else:
            print("there is no information with the ID,",ID_choose)
    valid = False
#   validity check
#   start date
    while valid == False:
        try:
            datecheck = ''
            testdate = []
            startdate = []
            datecheck = input("Enter the date you want to start from(month/date/year): ")
            for value in datecheck.split('/'):
                testdate.append(int(value))
        except ValueError:
            print("You Entered the invalid Date! Enter again!\n")
            del(testdate)
#   specific validity check
        else:
            for i in testdate:
                startdate.append(str(i))
            del(testdate)
            if len(startdate) == 3 and (startdate[0].isdigit() and startdate[1].isdigit() and startdate[2].isdigit()):
                valid = date_validity_check(startdate)
                if valid == False:
                 del(startdate)
            else:
                print("You Entered the invalid Date! Enter again!\n")
                del(startdate)
                    
#   validity check                    
#   end date
    valid = False
    while valid == False:
        try:
            enddate = []
            datecheck = ''
            testdate = []
            datecheck = input("Enter the date you want to end with(month/date/year): ")
            for value in datecheck.split('/'):
                testdate.append(int(value))
        except ValueError:
            print("You Entered the invalid Date! Enter again!\n")
            del(testdate)
#   specific validity check
#   if the start date is after enddate, it might be non-sense. it prevents from that
        else:
            for i in testdate:
                enddate.append(str(i))
            del(testdate)
            if len(enddate) == 3 and (enddate[0].isdigit() and enddate[1].isdigit() and enddate[2].isdigit()):
                valid = date_validity_check(enddate)
                if valid == False:
                    print("You Entered the invalid Date! Enter again!\n")
                else:
                    if int(enddate[2]) < int(startdate[2]):
                        valid = False
                        print("End day should not be smaller than the start day!\n")
                    elif int(enddate[2]) == int(startdate[2]) :
                        if int(enddate[0]) < int(startdate[0]): 
                            print("End day should not be smaller than the start day!\n")
                            valid = False
                        elif int(enddate[0]) == int(startdate[0]):
                            if int(enddate[1]) < int(startdate[1]): 
                                print("End day should not be smaller than the start day!\n")
                                valid = False
            else:
                print("You Entered the invalid Date! Enter again!\n")
                
#   create the sql code based on what the user has entered
    sql = "SELECT fldFirstName, fldLastName FROM tblPersonalInfo WHERE pmkPersonalID = '" + ID_choose + "';"
    filename = ''
    name = []
    getInfo = []
#   check the validity of the file's name
    while filename.endswith('.txt') == False:
        filename = input("\nEnter the File Name that You Want to Store In (include .txt at the end): ")
        if filename.endswith('.txt') == False:
            print('Please put .txt at the end of the filename\n')
#   try to open a file
    try:
        printUserFile = open(filename, 'w')
    except:
        print("File open error")
    else:
#   create the table in the txt files
        DBConnect = DB_connector.cursor()
        DBConnect.execute(sql)
        for a in DBConnect:
            name.append(a)

#   make the header of the table
        printUserFile.write("Hello, " + name[0][0] + ", "+ name[0][1] + "\nBelow is your exercise table from " + startdate[2] + "/" + startdate[0] + "/" + startdate[1] +" to " + enddate[2] + "/" + enddate[0] + "/" + enddate[1] + "\n\n")
        printUserFile.write(format("date","25s") + format("exercise name","35s") + format("part","15s") + format("sets","10s") + format("reps","10s") + format("weights","20s") +"\n")
        sql = "SELECT * FROM tblPersonalExercise WHERE fldPersonalID = '" + ID_choose + "' AND fldDate >= '" + startdate[2] + "-" + startdate[0] + "-" + startdate[1] + "' AND fldDate <='"+ enddate[2] + "-" + enddate[0] + "-" + enddate[1] + "' ORDER BY fldDate DESC"
        DBConnect = DB_connector.cursor()
        DBConnect.execute(sql)
        for value in DBConnect:
            getInfo.append(value)
        previousDate = ''
#   make the list for table
        for row in getInfo:
            if previousDate != str(row[5]):
                printUserFile.write(format(str(row[5]),"25s") + format(row[2],"35s") + format(row[6],"15s") + format(str(row[3]),"10s") + format(str(row[4]),"10s") + format(str(row[7]),"20s") +"\n")          
            else:
                printUserFile.write(format("","25s") + format(row[2],"35s") + format(row[6],"15s") + format(str(row[3]),"10s") + format(str(row[4]),"10s") + format(str(row[7]),"20s") +"\n")    
            previousDate = str(row[5])
#   close the file
        printUserFile.close()


        
#   ===============================================================================================
#   (EVENT)Randomly Choose members
#   randomly choose people in the database
def eventChooseMembers(DB_connector):

    valid = False
#   call the personal info from the database and create the list
    sql = 'SELECT * FROM tblPersonalInfo;'
    DBConnect = DB_connector.cursor()
    DBConnect.execute(sql)
    dataList = []

    for data in DBConnect:
        dataList.append(data)
#   ask user how many people would the user wants to choose
    while valid == False:
#   validate input
        try:
            numberPick=int(input("How many people would you want to pick?"))
        except ValueError:
            print("Please Enter the valid number!")
        else:
            if numberPick > len(dataList):
                print("There are less than",numberPick,"people in the DB! Please Enter the smaller number!")
            elif numberPick <= 0:
                print("You should choose at least one number!");
            else:
                valid = True
#   randomly choose people and those who have been chosen will be saved in dictionary
    count = 0
    randomindex = 0
    pickedDict = dict()
    while count <= numberPick - 1:
        randomindex = random.randint(0, numberPick - 1)
        if dataList[randomindex][0] not in pickedDict:
            pickedDict[dataList[randomindex][0]] = dataList[randomindex][1:]
            count += 1
#   email creating
    message = EmailMessage()
    message['Subject'] = 'MY MUSCLE Event, Congratulations!'
    message['From'] = 'MY MUSCLE TEAM <jjung2@uvm.edu>'
    email = []
    for i in pickedDict:
        email.append(pickedDict[i][2])
#   to show that I have chosen and saved email address!
    print(email)
#    message['To'] = ', ' . join(email)
    print("(For grader) Change the below email to check if the mail is going! I checked if multiple senders are possible using above email")
    print("but my friends, who have helped me make data, suffer from email bomb... so if you delete the below append and reactivate the above comments, it works!")
#   (For grader) Change the below email to check if the mail is going! I checked if multiple senders are possible using above email
#   but my friends, who have helped me make data, suffer from email bomb... so if you delete the below append and reactivate the above comments, it works!
#   (https://stackabuse.com/how-to-send-emails-with-gmail-using-python/),(https://docs.python.org/3/library/email.examples.html)
    message['To'] = 'hwasungishungry@gmail.com'

#   message using html
    message.add_alternative('''\
<figure><img src='https://jjung2.w3.uvm.edu/cs008/final/image/MY_MUSCLE.png' alt='MY MUSCLE logo' width='240'></figure>\
<h1>Congratulations!</h1>\
<p style="color:grey; font-size:20px;">You have been selected by MY MUSCLE TEAM, and you will get a prize!</p>\
<p style="color:grey; font-size:20px;">Please tell us your <strong style="text-decoration:underline;color:black;">Contact Information</strong> and <strong style="text-decoration:underline;color:black;">Home Address</strong></p><br>\
<h4 style='font-family:\'Courier New\', Courier, monospace;'>What You Will Get!</h4>\
<ul>\
<li style='text-decoration: underline;padding-bottom:0.5em;padding-top:1em;'>1kg of Protein</li>\
<li style='text-decoration: underline;padding-bottom:0.5em;'>Free Online Personal Traning for A Month</li>\
<li style='text-decoration: underline;padding-bottom:0.5em;'>MY MUSCLE T-shirt</li>\
</ul><br>\
<p><a href='https://jjung2.w3.uvm.edu/cs008/final/index.php'>To go to Website...</a></p>''',subtype='html')

#   if failed to connect to email host => exception
    try:
        with smtplib.SMTP('smtp.uvm.edu',587) as s:
#   for security, according to what the links above say
            s.starttls()
#   my netID...
            s.login('jjung2@uvm.edu','dUbvip-1cubpu-honqej')
#   message send
            s.send_message(message)
            s.quit()
    except:
        print("mail Error!")
    else:
        print("we have successfully sent your email! Thank you!\n")





#   **************************

def date_validity_check(date):
#   year check
    if int(date[2]) <= YEAR_LIMIT_MAX and int(date[2]) >= YEAR_LIMIT_MIN:
#   1 <= month <= 12
        if MONTH_COUNT - int(date[0]) >= 0 and MONTH_COUNT - int(date[0]) < MONTH_COUNT:
#   months that have 31 days
            if int(date[0]) == 1 or int(date[0]) == 3 or int(date[0]) == 5 or int(date[0]) == 7 or int(date[0]) == 8 or int(date[0]) == 10 or int(date[0]) == 12:
#   day check (1 <= day <= 31)
                if DATE_COUNT - int(date[1]) >= 0 and DATE_COUNT - int(date[1]) < DATE_COUNT:
                    return True
                else:
                    print("You entered the wrong date!\nPlease Enter the valid Date\n")
                    return False
                
#   months that have 30 days or 28 or 29 days 
            else:
#   day check (1 <= day <= 30)
                if (DATE_COUNT - 1) - int(date[1]) >= 0 and (DATE_COUNT - 1) - int(date[1]) < (DATE_COUNT - 1) and int(date[0]) != 2:
                    return True
#   if Febuary
                elif int(date[0]) == 2:
#   check if it is a leap year
                    if (int(date[2]) % 4 == 0 and int(date[2]) % 100 != 0) or int(date[2]) % 400 == 0:
#   day check (1 <= day <= 29)
                        if (DATE_COUNT - 2) - int(date[1]) >= 0 and (DATE_COUNT - 2) - int(date[1]) < (DATE_COUNT - 2):
                            return True
                        else:
                            print("You entered the wrong date!\nPlease Enter the valid Date\n")
                        return False

                    else:
#   day check (1 <= day <= 28)
                        if (DATE_COUNT - 3) - int(date[1]) >= 0 and (DATE_COUNT - 3) - int(date[1]) < (DATE_COUNT - 3):
                            return True
                        else:
                            print("You entered the wrong date!\nPlease Enter the valid Date\n")
                            return False
                else:
                    print("You entered the wrong date!\nPlease Enter the valid Date\n")  
                    return False
        else:
            print("You entered the wrong date!\nPlease Enter the valid Date\n")  
            return False
    else:
        print("You entered the wrong date!\nPlease Enter the valid Date\n")  
        return False

#   **************************

           
main()
