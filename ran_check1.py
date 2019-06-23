'''
To check an integer is within the range 
'''


#Function 
def ran_check(num, high, low):
    if low<=num<=high:
        return 'within the range'
    else:
        return 'out of range'

a = int(input('Enter a number \n'))
b = int(input('Enter low number \n '))
c = int(input('Enter high number \n')) 
result = ran_check(a, c, b)
print (f'The number {a} is {result} between the {b} and {c}')
