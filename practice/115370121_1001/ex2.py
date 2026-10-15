##find the max value from 3 numbers

num1=float (input("enter first number:"))
num2=float (input("enter second number:"))
num3=float (input("enter third number:"))

if num1>num2 and num1>num3:
    max_value=num1
elif num2>num1 and num2>num3:
    max_value=num2
else:
    max_value=num3

print("the max value is:", max_value)