'''
Program to divide two numbers
'''
#try and except is used to get integers as input 
while True:
    x = int(input("Enter the number 1\n"))
    y = int(input("Enter the number 2\n"))
    try:
        z = x/y
        print (z)
        break
    #ZeroDivisionError comes when the denominator is zero
    except ZeroDivisionError:
        print("division is not possible when denominator is zero\n")
        print("Enter the integer other than zero\n")
        continue
    #Other errors(when any character is entered instead of integer)
    except:
        print("Enter valid integer\n")
    finally:
        print("All Done")
