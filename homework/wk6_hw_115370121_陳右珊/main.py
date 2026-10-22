from parking import fee, records, report


n = int(input("車次 n(1~50):"))
while n < 1 or n > 50:
	n = int(input("超出範圍，請重新輸入："))

seed = int(input("亂數種子："))
record_lines = records.generate_records(n, seed)
fees = []
free_count = 0

for line in record_lines:
	plate, t_in, t_out, minutes, is_member = records.parse_record(line)
	parking_fee = fee.calc_fee(minutes, is_member)
	fees.append(parking_fee)
	if parking_fee == 0:
		free_count += 1
	print(report.format_line(plate, t_in, t_out, minutes, is_member, parking_fee))

total, average, highest = report.summary(fees)
print(f"總車次 = {n}，免費 = {free_count}")
print(f"總收入 = {total} 元，平均 = {average:.1f} 元，最高 = {highest} 元")
