'''
Return true if number 3 is exist successively for 2 times
'''

#Function definition
def has_33(nums):
    for i in range(0, len(nums) - 1):
                   return [nums[i],nums[i+2]] == [3,3]
    

a = [int(x) for x in input('Enter the list\n').split()]
result = has_33(a)
print (result)
