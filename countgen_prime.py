'''
code for counting the prime numbers and generating the prime numbers within the given n interger
'''
#Function to generate prime numbers
def prime(num):
    prime = [2]
    for i in range(3,num):
        for j in range(2,i-1):
            if i%j == 0:
              break
        else:    
            prime.append(i)      
            
    return prime


a = int(input("Enter a number \n"))
result = prime(a) #Function call to generate prime numbers
count = len(result) #Counting the prime numbers using len() function
print (f'The number of prime numbers is {count}\n')
print (f'The prime numbers within {a} are {result}')

