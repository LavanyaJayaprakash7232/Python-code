'''
Program to check whether the given input integer is prime number or not!
'''
#Function to check the prime number
def check_prime(num):
    count = 0
    for i in range(2, num-1):
            if num%i != 0:
               continue
            else:
               return "not a prime number"
               break
    return "prime number"   

#User input
a = int(input('Enter a number \n'))
#Function call
result = check_prime(a)
#Output
print (f'{a} is a {result}')
