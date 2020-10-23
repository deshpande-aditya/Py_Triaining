#Reading files like anything these days. :P
'''

#This code also works and is awesome
employee_file = open("employees-excel.xls", 'r')
try:
    #print(employee_file.readable())
    #print(employee_file.readline())
    #print(employee_file.readline())
    #print(employee_file.readline())
    num = int(input("Enter row number to read :"))
    print(employee_file.readlines()[num])
except IndexError as err1:
    print(err1)
except ValueError as err2:
    print(err2)

employee_file.close()

'''

'''
#reading file again in different way
employee_file = open("employees.txt", 'r')
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
'''
#Writing new files and appending files.
employee_file = open("employees.txt", 'a')
employee_file.write("\nKross - Customer care")
employee_file.close()