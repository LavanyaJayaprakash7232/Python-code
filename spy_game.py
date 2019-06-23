'''
Get the list
To check whether the numbers 0 0 7 exists successively in the list
'''

#Function to check 007
def spy_game(mylist):
    a = 0
    for i in range(0, len(mylist)-2):
        if [mylist[i],mylist[i+1],mylist[i+2]] == [0,0,7]:
           a = 1
           break
    if a == 1:
       return True
    else:
        return False
    
a = [int(x) for x in input("Enter the list\n").split()]
result = spy_game(a)
print (result)

            
