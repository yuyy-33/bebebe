height=float(input("請輸入身高："))
weight=float(input("請輸入體重："))

bmi= float(weight)/((float(height)/100)**2)

if bmi<18.5:
    print("體重過輕")
elif bmi>=18.5 and bmi<24:
    print("體重正常")
elif bmi>=24 and bmi<27:
    print("體重過重")
elif bmi>27:
    print("肥胖")

