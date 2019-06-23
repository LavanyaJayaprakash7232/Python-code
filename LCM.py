'''
To find the LCM of two given numbers
'''

#Function to find LCM
def lcm(num1, num2):
    if num1>num2:
        r = num1
    else:
        r = num2

    while True:
        if r%num1 == 0 and r%num2 == 0:
             lcm = r
             break
        r = r+1

    return lcm

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))
result = lcm(num1, num2)
print(result)
        
