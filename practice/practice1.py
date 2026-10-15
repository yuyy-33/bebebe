"""
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

print(1, 2, 3, sep="-") # 1-2-3
print("不換行", end=" ")
print("接在同一行")
print("換行")


number =[1, 2, 3]
print(number)  # [1, 2, 3]
number.insert(3, 4)
print(number)  # [1, 2, 3, 4]
number.insert(0, 0)
print(number)  # [0, 1, 2, 3, 4]
number.remove(2)
print(number)  # [0, 1, 3, 4]
number.pop(0)
print(number)  # [1, 3, 4]


name= str(input("請輸入英文名字："))
print(len(name))
print(name.upper())
print(name.startswith("A"))
"""

# nums=[5,3,8,1,9]
# nums.append(20)
# nums.remove(3)
# print(sorted(nums)) #小到大
# print(sorted(nums, reverse=True)) #大到小

# p1=(2,3)
# p2=(5,7)
# x=p2[0]-p1[0]
# y=p2[1]-p1[1]
# print(x,y)

# book={}
# book["小明"]="0912345678"
# print(book.get("小黃","error"))


