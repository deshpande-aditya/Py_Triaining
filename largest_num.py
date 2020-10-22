
#find largest of 3 numbers
def max_num(x, y, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    else:
        return z


n1=input("Enter first Number: ")
n1_ = int(n1)
print(n1_)

n2=input("Enter second Number: ")
n2_ = int(n2)
print(n2_)

n3=input("Enter third Number: ")
n3_ = int(n3)
print(n3_)

max = max_num(n1_ ,  n2_ , n3_)
print("Maximum of 3 entered numbers is :" + str(max))