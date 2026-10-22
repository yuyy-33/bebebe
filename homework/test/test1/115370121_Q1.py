name=(input("請輸入你的姓名："))
kg=(float(input("請輸入你的體重：")))
height=(float(input("請輸入你的身高：")))

m=(height/100)
BMI=kg/(m*m)
hope=(m*m)*22
dis=kg-hope

print(f"{name}的BMI={BMI:.2f}")
print(f"理想體重＝{hope:.2f}公斤")
print(f"體重差距＝{dis:.2f}公斤")
