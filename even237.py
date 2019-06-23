'''
To print even numbers in the given list.
It should skip the numbers present after the integer 237
'''

#Function for generating only the even numbers in the list till it encounters 237
def even237(num):
    for i in num:
        if i%2 == 0:
            print(i)
        if i == 237:
            break

#User input and output
num = [int(x) for x in input("Enter the list of numbers\n").split()]
result = even237(num)
