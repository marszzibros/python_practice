#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   lists and tuples
def main():
#   list
    years = [2016, 1620, 1984, 1776, 1860, 1492]
#   Part one a. print a type of the list 'years'    
    print(type(years))
#   Part one b. 
    print(years)
#   Part one c.
    print(years[0])
#   Part one d.
    print(years[2:5])
#   Part one e.
    print("Minimum value:", min(years), "\nMaximum Value:", max(years))
#   Part one f.
    for value in years:
        print(value)
#   Part one g.
    for i in range(0,len(years)):
        print('Yr',i,': ',years[i],sep='')

#   tuple /need to change [] => ()
    years2 = (2016, 1620, 1984, 1776, 1860, 1492)
#   Part one a. print a type of the list 'years'    
    print(type(years2))
#   Part one b. 
    print(years2)
#   Part one c.
    print(years2[0])
#   Part one d.
    print(years2[2:5])
#   Part one e.
    print("Minimum value:", min(years2), "\nMaximum Value:", max(years2))
#   Part one f.
    for value in years2:
        print(value)
#   Part one g.
    for i in range(0,len(years2)):
        print('Yr',i,': ',years2[i],sep='')

#   replace years (list) value 1860 to 1865
    years[4] = 1865
    print(years[4])

#   try & except with tuple
    try:
        years2[4] = 1865
    except TypeError:
        print('you cannot modify the tuple')

#   use the romove methods to remove 1984
    years.remove(1984)
    print(years)
#   tuple cannot use remove
#   sort
    years.sort()
    print(years)
#   sort reverse
    years.sort(reverse=True)
    print(years)
#   tuple cannot use sort

#   create a dorm and verify if it is empty
    dorms=[]
    print(len(dorms))
#   use append
    dorms.append('Converse')
    print(dorms)
#   use inserts to put in the index 0
    dorms.insert(0, "Mason")
    print(dorms)

#   add values
    dorms.append(['UHeights','Redstone','Trinity'])
    print(dorms[2],type(dorms[2]))
    dorms += ['Christie','Wright','Patterson']
    print(dorms)

#   Given the following code
    central = ["WE", "Converse"]
    athletic = ["UHeights", "Harris/Millis", "MAT", "L/L"]
    redstone = ["CWP","SMH","WDW"]
    housing = [central, athletic, redstone]
    print(type(housing))
    print(type(housing[0]))
    print(type(housing[0][0]))
    print(housing[housing.index(athletic)][athletic.index("MAT")])

#   Part three
#   odd number between 51-67
    odds = []
    for i in range(51,68,2):
        odds.append(i)
    print(odds)
#   even number between 51-67
    evens = []
    for i in range(2, 11, 2):
        evens.append(i)
    print(evens)
#   concatenate    
    nums = odds + evens
    print(nums)
#   nums2 = nums
    nums2 = nums
#   delete nums 6th element
    del(nums[5])
    print(nums)
    print(nums2)
#   it both disappears!
#   print real copy
    nums2 = []
    for val in nums:
        nums2.append(val)
#   delete 6th element    
    del(nums[5])
    print(nums)
    print(nums2)
#   it becomes real 'copy'(nums change does not affect nums2)

main()