'''
Generating unique list of integers
'''

#Function to generate unique elements using 'set'
def unique_list(mylist):
    return set(mylist) #set - {unique representation}

a = [int(x) for x in input('Enter a list \n').split()]
result = unique_list(a)
print (result)

