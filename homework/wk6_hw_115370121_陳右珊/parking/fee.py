import math
DAY_MIN = 1440
FREE_MIN = 30
BLOCK_MIN = 30
BILL_PER_BLOCK = 20
DAILY_MAX = 300

def calc_fee(minutes: int, is_member: bool = False) -> int:
    """依停車分鐘數與會員身分計算停車費。"""
    full_days, remaining_minutes = divmod(minutes, DAY_MIN)
    bill = full_days * DAILY_MAX

    if remaining_minutes > FREE_MIN:
        blocks = math.ceil(remaining_minutes / BLOCK_MIN)
        bill += min(blocks * BILL_PER_BLOCK, DAILY_MAX)

    if is_member:
        bill = round(bill * 0.8)
    return bill


if __name__ =="__main__":
    tests = [
            (30, False, 0),
            (31, False, 40),
            (60, False, 40),
            (61, False, 60),
            (145, True, 80),
            (600, False, 300),
            (600, True, 240),
            (1500, False, 340),
            (1500, True, 272),
        ]
    for minutes, is_member, expected in tests:
        result = calc_fee(minutes, is_member)
        if result == expected:
            print("OK")
        else:
            print("錯")
       


