##try except :input a number,and catch error
try:
    n=int(input("enter a number:"))
    print(10/n)
except ValueError:
    print("please enter a value integer.")
except ZeroDivisionError:
    print("cannot divide by zero.")