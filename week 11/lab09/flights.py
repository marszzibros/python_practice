#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   Lab09 - flights.py
def main():
#   refers the dictionary
    flights = {'Burlington':['Boston', 'New York', 'Los Angeles'],
               'New York': ['Los Angeles', 'Fort Lauderdale','Boston'],
               'Boston' : ['Montreal','Memphis','Washington'],
               'Washington' : ['Boston', 'San Diego'],
               'Los Angeles' : ['San Diego', 'Boston', 'Washington'],
               'Montreal': ['Boston','Fort Lauderdale'],
               'Fort Lauderdale' : ['Boston', 'Montreal'],
               'Memphis': ['Boston'],
               'San Diego': ['Los Angeles', 'Washington']
    }
#   check if the user enters the valid file name
    valid = False
    while valid == False:
        cityName = input("What airport are you leaving from? ")
#   if the cityname is not in flights => print so that user can enter again
        if cityName not in flights:
            print("you entered the wrong airport! Please check again!")
#   or go out of the while loop
        else:
            valid = True
#   print statements
    print("Departing from",cityName, "you can reach the following destinations with zero or one connections")
#   get value from certain key
    for city in flights[cityName]:
        print(city, "dircet")

#   use these values as a key
        for secondConnection in flights[city]:
#   print the values inside the key
            print(secondConnection, "via", city)

main()

