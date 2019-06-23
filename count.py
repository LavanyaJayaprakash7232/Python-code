'''
To count the number of times of presence of particular character in a given list
'''
#Funtion to count the given integer in the list
def count(num, n):
    count = 0
    for i in num:
        if(n == i):
            count = count+1
    return count

#User input to get list
mylist = [int(x) for x in input("Enter the list of integers\n").split()]
#User input to get the number 
a = int(input("Enter the number you want to check\n"))
#Function call and output
result = count(mylist, a)
print(f'Count of {a}:\t{result}')    
