#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   FINAL PROJECT - GYM recorder admin

#   import library mysql.connector (https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)
#   for connecting mysql and Python
import mysql.connector
import random
#   phpMyAdmin ID and Password
DB_ID = 'jjung2_admin'
DB_PASSWORD = 'UzAn4dsM6VIZigk1'

connection = False
try:

    DB_connector = mysql.connector.connect(
        host = "webdb.uvm.edu",
        user = DB_ID,
        password = DB_PASSWORD,
        database = "JJUNG2_database")
except:
    print('DB connection error! Please Enter the valid ID & Password! \n')   
else:
    connection = True
    print("Successfully connected to Database!")
    sql = "SELECT (pmkPersonalID) FROM tblPersonalInfo"
    DBConnect = DB_connector.cursor()
    DBConnect.execute(sql)
    userID = []
    for value in DBConnect:
        userID.append(value[0])
    sql = "SELECT fldExercise, fldPart FROM tblExerciseSteps GROUP BY fldExercise"
    DBConnect = DB_connector.cursor()
    DBConnect.execute(sql)
    partExercise = dict()
    for value in DBConnect:
        if value[1] in partExercise:
            partExercise[value[1]].append(value[0])
        else:
            partExercise[value[1]] = list()
            partExercise[value[1]].append(value[0])
    for name in userID:
        weight = int(input("weight: "))
        
        for i in range(1,31):
            partRan = random.randint(1,3)
            sql = 'INSERT INTO tblPersonalExercise (fldPersonalID, fldExerciseName, fldPart, fldExerciseRepsPerSet,fldSetRepeat,fldDate,fldWeight) VALUES ("' + name + '",'
            if partRan == 1:
                exerciseRan = random.randint(0,2)
                sql += ('"'+ partExercise['Chest'][exerciseRan]+'"')
                sql += ', "Chest"'
                reps = random.randint(1,20)
                sql += ',' + str(reps)
                sets = random.randint(1,5)
                sql += ',' + str(sets)
                sql += ',"2020-11-'+ str(i)+'"'  
                if partExercise['Chest'][exerciseRan] != 'Push-up':
                    sql += ','+ str(weight) + ')'
                else:
                    sql += ', 0)' 
                weight += 2.3
            elif partRan == 2:
                exerciseRan = random.randint(0,2)
                sql += ('"'+ partExercise['Legs'][exerciseRan]+'"')
                sql += ', "Legs"'
                reps = random.randint(1,20)
                sql += ',' + str(reps)
                sets = random.randint(1,5)
                sql += ',' + str(reps)
                sql += ',"2020-11-'+ str(i)+'"'  
                sql += ','+ str(weight) + ')'
                weight += 2.3
            elif partRan == 3:
                exerciseRan = random.randint(0,2)
                sql += ('"'+ partExercise['Back'][exerciseRan]+'"')
                sql += ', "Back"'
                reps = random.randint(1,20)
                sql += ',' + str(reps)
                sets = random.randint(1,5)
                sql += ',' + str(sets)
                sql += ',"2020-11-'+ str(i)+'"'  
                if partExercise['Back'][exerciseRan] != 'Pull-up':
                    sql += ','+ str(weight) + ')'
                else:
                    sql += ', 0)' 
                weight += 2.3
            print(sql)
            DBConnect = DB_connector.cursor()
            DBConnect.execute(sql)
            DB_connector.commit()





    
    

        