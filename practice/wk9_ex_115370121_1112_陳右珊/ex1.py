
print("===== Python 小計算機 =====")

num1 = float(input("請輸入第一個數字："))
num2 = float(input("請輸入第二個數字："))

print("請選擇運算方式：")
print("1. 加法 +")
print("2. 減法 -")
print("3. 乘法 *")
print("4. 除法 /")

choice = input("請輸入選項 (1-4)：")

if choice == "1":
    print("答案：", num1 + num2)
elif choice == "2":
    print("答案：", num1 - num2)
elif choice == "3":
    print("答案：", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("答案：", num1 / num2)
    else:
        print("錯誤：不能除以 0！")
else:
    print("無效的選項！")
