'''
To calculate the volume of sphere
'''
 #Function to calculate volume
def volume(radius):
    return 4/3*22/7*radius
    

a = int(input('Enter the radius \n'))
result = volume(a)
print (f'The volume of sphere is {result}')
