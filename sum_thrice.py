'''
Get three integers
Return their sum if the numbers are distinct
Return thrice the sum if the numbers are same
'''

#Function sum thrice
def sum_thrice(a, b, c):
    if(a==b==c):
       return (a+b+c)*3
    else:
       return a+b+c

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))
num3 = int(input("Enter the number 3\n"))
result = sum_thrice(num1, num2, num3)
print(result)
