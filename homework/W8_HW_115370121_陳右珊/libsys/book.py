from datetime import timedelta


class Book:
    count = 0
    LOAN_DAYS = 14

    def __init__(self, book_id, title, author, category, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.borrower = None
        self.due = None
        self.times = 0
        Book.count += 1

    @staticmethod
    def parse_line(line):
        fields = [field.strip() for field in line.rstrip("\n").split(",")]
        if len(fields) != 5:
            raise ValueError("書目欄位數錯誤")

        book_id, title, author, category, year_text = fields
        try:
            year = int(year_text)
        except ValueError as error:
            raise ValueError("出版年不是整數") from error
        return book_id, title, author, category, year

    @classmethod
    def total(cls):
        return cls.count

    def is_borrowed(self):
        return self.borrower is not None

    def borrow(self, reader, date):
        if self.is_borrowed():
            return False, "已借出"

        self.borrower = reader
        self.due = date + timedelta(days=self.LOAN_DAYS)
        self.times += 1
        return True, "成功"

    def return_book(self, date):
        if not self.is_borrowed():
            return False, "未借出"

        overdue_days = max(0, (date - self.due).days)
        self.borrower = None
        self.due = None
        return True, overdue_days

    def __str__(self):
        return f"{self.book_id} {self.title}（{self.author}，{self.year}）"


class ReferenceBook(Book):
    def borrow(self, reader, date):
        return False, "參考書不外借"
