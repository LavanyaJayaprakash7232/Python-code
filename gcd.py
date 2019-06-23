'''
To determine the Greatest Common Divisor for the given two integers
'''

#Function to calculate gcd
def gcd(num1, num2):
    p = 1
    if num1%num2 == 0:
        return num2
    for k in range(int(num2/2), 0, -1):
        if num1%k == 0 and num2%k == 0:
            p = k
            break
    return p
    

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))
result = gcd(num1, num2)
print(result)
        
