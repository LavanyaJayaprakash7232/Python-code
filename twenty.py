'''
Get two integers
Return true if the sum of numbers or any one of the number is twenty
'''

#Function 
def makes_twenty(num1, num2):
    return num1 + num2 == 20 or num1 == 20 or num2 == 20
        
a = int(input("Enter a number \n"))
b = int(input("Enter another number \n"))
output = makes_twenty(a,b)
print(output)
