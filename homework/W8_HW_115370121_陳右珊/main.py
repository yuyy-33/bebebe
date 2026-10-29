from datetime import datetime
from pathlib import Path

from libsys import Book, Library


base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data"

library = Library()
library.load_books(data_dir / "books.csv")
check_date = datetime.strptime(input(), "%Y-%m-%d").date()
failed_records = library.process(data_dir / "loans.txt")

for record in failed_records:
    print(record)

report_lines = library.report(check_date)
for line in report_lines:
    print(line)

print(f"（共建立 {Book.total()} 個 Book 物件）")

with open(base_dir / "report.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(report_lines) + "\n")

print("已寫入 report.txt")