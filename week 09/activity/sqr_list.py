#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   warmup task01: squaring list numbers

def main():
#   set lists
    list1 = [1,2,3,4,5,6,7]
    list2 = []
#   using for loop, append it    
    for num in range(0,len(list1)):
        list2.append(list1[num] ** 2)
#   print
    print(list2)
main()