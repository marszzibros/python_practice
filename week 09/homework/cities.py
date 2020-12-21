#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   HW 08-02 city check

#   main function
def main():
#   refer the variables
    city_name = 'a'
#   if there is a letter in file, make it True, unless False
    newHamp = False
    vermont = False
#   call file2list and get a list
    vtList = file2list('vt_municipalities.txt')
    nhList = file2list('nh_municipalities.txt')
#   if there is not anything at least in one file...
    if not(len(vtList) == 0 or len(nhList) == 0):
#   until the city_name is q
        while city_name != 'q':
            city_name = input("City name (type 'q' to quit):")
#   if the city is int the vt, vermont = True         
            if city_name in vtList:
                vermont = True
#   if the city is int the nh, newhampshire = True         
            if city_name in nhList:
                newHamp = True

#   if the city in both state        
            if vermont and newHamp:
                print(city_name,'is in Vermont and New Hampshire.\n')
                newHamp = False
                vermont = False
#   if the city is only in vt
            elif vermont and not newHamp:
                print(city_name,'is in Vermont.\n')
                vermont = False
#   if the city is only in nh
            elif not vermont and newHamp:
                print(city_name,'is in New Hampshire.\n')
                newHamp = False
#   if neither
            elif not(vermont and newHamp) and city_name !='q':
                print('Neither VT nor NH has a city by that name.\n')

#   function file2list: read txt file        
def file2list(fileName):
#   empty list    
    citylist= []
#   try to open a file
    try:
        mylist = open(fileName, 'r')
#   error
    except IOError:
        print("***FILE ERROR:",fileName,"cannot be found.")
#   or get the txt file as a list    
    else:
        for val in mylist:
            citylist.append(val.rstrip('\n'))
        mylist.close()
#   return the list

    return citylist
#   call main function
main()
