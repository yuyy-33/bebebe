a=int(input("購買Ａ的數量："))
b=int(input("購買Ｂ的數量："))
a=a*100
b=b*150
total=float(a+b)*0.85
print(f"總金額為：${total:.2f}")