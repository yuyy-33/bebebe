from datetime import datetime

from .book import Book, ReferenceBook


class Library:
    MAX_LOANS = 3
    REASONS = ["已借出", "未借出", "查無此書", "參考書不外借", "超過借閱上限"]

    def __init__(self):
        self.books = {}
        self.category_counts = {}
        self.book_format_errors = 0
        self.loan_format_errors = 0
        self.successes = 0
        self.failures = 0
        self.failure_counts = {reason: 0 for reason in self.REASONS}
        self.late_returns = 0
        self.reader_loans = {}

    def load_books(self, path):
        with open(path, "r", encoding="utf-8") as file:
            next(file, None)
            for line in file:
                if not line.strip():
                    continue
                try:
                    book_id, title, author, category, year = Book.parse_line(line)
                except ValueError:
                    self.book_format_errors += 1
                    continue

                book_class = ReferenceBook if category == "參考書" else Book
                self.books[book_id] = book_class(
                    book_id, title, author, category, year
                )
                self.category_counts[category] = (
                    self.category_counts.get(category, 0) + 1
                )

    def process(self, path):
        failed_records = []
        with open(path, "r", encoding="utf-8") as file:
            next(file, None)
            for line in file:
                if not line.strip():
                    continue
                fields = [field.strip() for field in line.rstrip("\n").split(",")]
                if len(fields) != 4:
                    self.loan_format_errors += 1
                    continue

                date_text, action, book_id, reader = fields
                try:
                    loan_date = datetime.strptime(date_text, "%Y-%m-%d").date()
                except ValueError:
                    self.loan_format_errors += 1
                    continue
                if action not in ("借", "還"):
                    self.loan_format_errors += 1
                    continue

                reason = self._process_record(action, book_id, reader, loan_date)
                if reason is None:
                    self.successes += 1
                    continue

                self.failures += 1
                self.failure_counts[reason] += 1
                failed_records.append(
                    f"{date_text} {action} {book_id} {reader}：失敗（{reason}）"
                )

        return failed_records

    def _process_record(self, action, book_id, reader, loan_date):
        book = self.books.get(book_id)
        if book is None:
            return "查無此書"

        if action == "借":
            if self.reader_loans.get(reader, 0) >= self.MAX_LOANS:
                return "超過借閱上限"

            succeeded, result = book.borrow(reader, loan_date)
            if not succeeded:
                return result
            self.reader_loans[reader] = self.reader_loans.get(reader, 0) + 1
            return None

        original_borrower = book.borrower
        if original_borrower is None or reader != original_borrower:
            return "未借出"

        succeeded, result = book.return_book(loan_date)
        if not succeeded:
            return result

        remaining = self.reader_loans.get(original_borrower, 0) - 1
        if remaining <= 0:
            self.reader_loans.pop(original_borrower, None)
        else:
            self.reader_loans[original_borrower] = remaining
        if result > 0:
            self.late_returns += 1
        return None

    def report(self, check_date):
        lines = [
            f"=== 圖書借閱報表（盤點日 {check_date:%Y-%m-%d}）===",
            (
                f"館藏 = {len(self.books)} 本（參考書 "
                f"{sum(isinstance(book, ReferenceBook) for book in self.books.values())} 本），"
                f"書目格式錯誤 = {self.book_format_errors}"
            ),
            (
                f"借還紀錄：成功 {self.successes}、失敗 {self.failures}、"
                f"格式錯誤 {self.loan_format_errors}"
            ),
            "失敗原因：" + "、".join(
                f"{reason} {self.failure_counts[reason]}" for reason in self.REASONS
            ),
            f"逾期歸還 = {self.late_returns} 筆",
        ]

        borrowed_books = [
            book for book in self.books.values() if book.is_borrowed()
        ]
        lines.append(f"--- 借出中（{len(borrowed_books)} 本）---")
        for book in borrowed_books:
            overdue_days = max(0, (check_date - book.due).days)
            status = f"逾期 {overdue_days} 天" if overdue_days else "未逾期"
            lines.append(
                f"{book.book_id} {book.title} {book.borrower} "
                f"應還 {book.due:%Y-%m-%d} {status}"
            )

        lines.append("--- 各類別館藏 ---")
        lines.extend(
            f"{category} {count} 本"
            for category, count in self.category_counts.items()
        )

        lines.append("--- 熱門書籍 Top 3 ---")
        popular_books = sorted(
            self.books.values(), key=lambda book: (-book.times, book.book_id)
        )[:3]
        lines.extend(
            f"{rank}. {book}　借閱 {book.times} 次"
            for rank, book in enumerate(popular_books, start=1)
        )
        return lines
