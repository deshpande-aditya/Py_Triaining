## check out some upcase logic with if statement.

name = input("Enter a name :")
name1 = name.upper()
#check if upper is working
print(name1)

if name.upper() == "ADITYA" or name.upper() == "AMRUTA":
    print("Welcome " + name +" !!")
else:
    print("You're not Aditya - get Lost!")
