def is_leap_year(year):
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


year_a, year_b = map(int, input().split())

for year in (year_a, year_b):
	if is_leap_year(year):
		print(f"{year} 是閏年")
	else:
		print(f"{year} 是平年")
        

a, b = map(int, input().split())

for year in (a, b):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("閏年")
    else:
        print("平年")