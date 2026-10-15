total_expense = float(input("請輸入總花費：")) ##日幣
people = int(input("請輸入人數："))
ex_rate=float(input("請輸入匯率：")) ##台幣／日幣：0.21

average_expense = total_expense / people##計算平均花費
average_expense_ntd = average_expense * ex_rate ##換算成台幣
print("平均花費為：",average_expense_ntd)##台幣花費

##tip rate 10%
tip_rate = 0.1
tip_amount = total_expense * tip_rate ##小費金額
ave_tip_amount = tip_amount / people ##每人小費金額
average_tip_amount_ntd = ave_tip_amount * ex_rate ##換算成台幣
print("平均提成為：",average_tip_amount_ntd)##台幣花費

##total expense with tip per person
total_expense_with_tip = average_expense_ntd + average_tip_amount_ntd ##每人花費加小費
print("每人平均花費（含提成）為：",total_expense_with_tip)##台幣花費