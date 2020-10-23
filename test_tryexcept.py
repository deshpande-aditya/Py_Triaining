'''
Try except - is used for exception handling,
please try running below code.
'''
try:
    num1=int(input("Enter an integer:"))
    value=10/0
    print(num1)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)