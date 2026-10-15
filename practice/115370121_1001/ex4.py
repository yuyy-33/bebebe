## BMI calculator based on your weight and height and gender
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
gender = input("enter your gender (male/female): ")

if gender =="male":
    standerd_weight=0.9*(weight**2)
    print("your standerd weight is:", standerd_weight)
    if standerd_weight>weight:
        print("you are underweight")
    elif standerd_weight<weight:
        print("you are overweight")
else:
    standerd_weight=0.8*(weight**2)
    print("your standerd weight is:", standerd_weight)
    if standerd_weight>weight:
        print("you are underweight")
    elif standerd_weight<weight:
        print("you are overweight")