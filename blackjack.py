'''
The function 'blackjack' adds the three integers.
Returns the sum if the sum is less than or equal to 21.
Else subtract 10 from the sum and returns.
'''

#Function to perform the above mentioned operation
def blackjack(num1, num2, num3):
    sum = num1 + num2 +num3
    if sum <=21:
        return sum
    elif sum > 21 or (num1 or num2 or num3) == 11:
        if sum - 10 <=21:
             return sum - 10
        else:
             return 'BUST'

#User input -> processing -> output
a = int(input("Enter a number \n"))
b = int(input("Enter next number \n"))
c = int(input("Enter last number \n"))
result = blackjack(a,b,c)
print (result)
