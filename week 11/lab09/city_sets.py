#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   lab09 - city_sets.py

#   main function
def main():

#   call file2list and get a set
    vtSet = set()
    nhSet = set()
    
#   get data from function
    nhSet.update(file2list('nh_municipalities.txt'))
#   length of nh
    print("There are", len(nhSet),"unique place names in NH\n")
    
#   get data from function
    vtSet.update(file2list('vt_municipalities.txt'))
    
#   length of vt
    print("There are", len(vtSet),"unique place names in VT\n")
#   Union of vt and nh
    print("There are",len(vtSet | nhSet),"unique place names in VT and NH combined.\n")
#   Intersection of vt and nh
    print("There are",len(vtSet & nhSet),"unique place names in VT and NH combined.\n")

    print("Here are the place names found in both VT and NH:")
    for intersectionCity in vtSet & nhSet:
        print(intersectionCity)
    print("\nHere are the place names found in VT and not NH:")
    print(len(vtSet.difference(nhSet)))
    for differenceCity in vtSet.difference(nhSet):
        print(differenceCity)
        
#   nhSet ^ vtSet: symetric difference
    mysteryset = nhSet ^ vtSet
    print(len(mysteryset),'\n')
#   replace the entry 'Burlington' to 'Bernietown'
    if 'Burlington' in vtSet:
        vtSet.discard('Burlington')
        vtSet.add('Bernietown')
#   Bernietown will not be added if I use update
    
#   create a list and sort and print
    vtlist = list(vtSet)
    vtlist.sort()
    for value in vtlist:
        print(value)
 
    
#   function file2list: read txt file        
def file2list(fileName):
#   empty list    
    citySet= set()
#   try to open a file
    try:
        mySet = open(fileName, 'r')
#   error
    except IOError:
        print("***FILE ERROR:",fileName,"cannot be found.")
#   or get the txt file as a set    
    else:
        citySet.update(mySet.read().split('\n'))
#   return the set
    return citySet
#   call main function
main()
