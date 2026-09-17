total=int(input("請輸入總金額："))
hundred = total // 100
total = total % 100
ten = total // 10
total = total % 10
print(f"100 元：{hundred} 張")
print(f"10 元：{ten} 張")
print(f"1 元：{total} 張")