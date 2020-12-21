#   Jay Hwasung Jung
#   CS 021 - B(GOLD)
#   In class Activity02

def main():
    listGrade=[92,89,76,68,72,90,87,97,85]

#   call function
#   get average using len function
    print(get_sum(listGrade))

#   function for summing
def get_sum(gradelist):
    total = 0

#   using for loop, sum it
    for i in gradelist:
        total += i
#   return average
    return total / len(gradelist)

#   call main function
main()