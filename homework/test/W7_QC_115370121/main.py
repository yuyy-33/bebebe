from qc import check, report


target_str, tol_str = input().split()
target = float(target_str)
tol = float(tol_str)

results = []
bad_streak = 0
count = 0

while True:
    value_str = input()
    if value_str == "end":
        break

    count += 1
    value = float(value_str)
    status = check.judge(value, target, tol)
    print(f"#{count} {value:.2f} {status}")
    results.append(status)

    if status == "OK":
        bad_streak = 0
    else:
        bad_streak += 1
        if bad_streak >= 3:
            print("連續 3 件不良，停線檢查")
            break

inspection_count, good_count, rate = report.summary(results)
print(f"檢驗數 = {inspection_count}")
print(f"良品數 = {good_count}")
print(f"良率 = {rate:.1f}%")
print(f"判定 = {report.decide(rate)}")
