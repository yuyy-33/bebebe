minute=int(input("請輸入幾分鐘："))
hour = minute // 60
minute = minute % 60
print(f"{hour} 小時 {minute} 分鐘")