'''
Program to get the list of integers as a input till they enter the integers
'''

#try and except is used
while True:
    mylist = input("Enter the list of integers\n").split()
    try:
        for i in mylist:
            print(int(i)**2)
        break
    
    except:
        print("Input invalid; Enter integers\n")
        

    finally:
        print("Thank you\n")



