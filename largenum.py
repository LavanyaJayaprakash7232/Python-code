'''
To find the largest number in the list
'''

mylist = [int(x) for x in input("Enter the list of integers\n").split()]
largenum = 0
for i in mylist :
    if i > largenum:
       largenum = i

print ("The largest number is", largenum)
