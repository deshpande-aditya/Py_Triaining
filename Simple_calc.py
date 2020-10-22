##Updated on seeing the trainings.

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
oper= input("Enter operator (+ - * /):")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid Operator.")
