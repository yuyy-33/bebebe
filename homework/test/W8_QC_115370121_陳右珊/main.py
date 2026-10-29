from pathlib import Path

from homework.test.W8_QC_115370121_陳右珊.stock import loader
from homework.test.W8_QC_115370121_陳右珊.stock import planner


base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"

while True:
    filename = input()
    try:
        items, format_errors = loader.load_items(data_dir / filename)
    except FileNotFoundError:
        print(f"找不到檔案：{filename}，請重新輸入")
        continue
    break

reorder_items, total_amount = planner.plan(items)

print(f"有效品項 = {len(items)}")
print(f"格式錯誤 = {format_errors}")
for name, quantity, amount in reorder_items:
    print(f"補貨 {name} {quantity} 個，金額 {amount:.1f}")
print(f"需補貨 = {len(reorder_items)} 項")
print(f"補貨總金額 = {total_amount:.1f}")

with open(base_dir / "reorder.csv", "w", encoding="utf-8") as file:
    file.write("品名,補貨量,金額\n")
    for name, quantity, amount in reorder_items:
        file.write(f"{name},{quantity},{amount:.1f}\n")

print("已寫入 reorder.csv")
