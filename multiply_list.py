'''
To multiply all the integers in the list
'''
#Function to multiply 
def multiply_list(mylist):
    product = 1
    for i in mylist:
        product = product * i
    return product

a = [int(x) for x in input("Enter the list \n").split()]
result = multiply_list(a)
print (f'The product of the integers in list is {result}')
        
