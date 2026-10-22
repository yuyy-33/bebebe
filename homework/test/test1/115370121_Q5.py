def calc_bill(kwh):
	if kwh <= 120:
		return kwh * 1.63
	if kwh <= 330:
		return 120 * 1.63 + (kwh - 120) * 2.38
	if kwh <= 500:
		return 120 * 1.63 + 210 * 2.38 + (kwh - 330) * 3.52
	return 120 * 1.63 + 210 * 2.38 + 170 * 3.52 + (kwh - 500) * 4.80


n = int(input("請輸入戶數："))
households = []
total = 0

for _ in range(n):
	kwh = int(input("請輸入用電度數："))
	bill = calc_bill(kwh)
	households.append((kwh, bill))
	total += bill
	print(f"{kwh} 度 -> {bill:.2f} 元")

print(f"總金額 = {total:.2f}")

if households:
	highest = max(households, key=lambda household: household[1])
	print(f"最高 = {highest[0]} 度（{highest[1]:.2f} 元）")
else:
	print("最高 = 無（0.00 元）")
