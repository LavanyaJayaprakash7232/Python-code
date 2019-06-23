'''
If two given integers are even, output should be minimum of two numbers
Else, output should be maximum of two numbers
'''

#Function to perform the above mentioned criteria
def op2(num1, num2):
    #If the two numbers are even, the function will return the minimum of two numbers
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    #Else it returns the maximum of two numbers
    else:
        return max(a,b)

    
a = int(input("Enter the number\n"))
b = int(input("Enter another number\n"))
output = op2(a,b)
print (output)
