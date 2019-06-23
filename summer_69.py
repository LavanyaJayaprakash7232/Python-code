'''
Get a list of integers
Sum all the integers in the list. Ignore integers from 6 - 9 
'''

#Function to sum
def summer_69(list):
    sum = 0
    if list == None:
        return 0 #Return Zero if the list is null
    for i in list:
        if 6<=i<=9:
           continue
        sum = sum + i
    return sum


print ('Enter the list\n')
a = [int(x) for x in input().split()]
result = summer_69(a)
print (result)        
