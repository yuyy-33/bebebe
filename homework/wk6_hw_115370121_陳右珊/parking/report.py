from datetime import datetime


def format_line(
	plate: str,
	t_in: datetime,
	t_out: datetime,
	minutes: int,
	is_member: bool,
	fee: int,
) -> str:
	"""將一輛車的停車資料格式化為報表的一行。"""
	member_label = "會員" if is_member else "一般"
	return (
		f"{plate} {t_in:%H:%M} -> {t_out:%H:%M} "
		f"{minutes:>4} 分 {member_label} {fee:>4} 元"
	)


def summary(fees: list[int]) -> tuple[int, float, int]:
	"""回傳總收入、平均收入與最高單筆金額。"""
	if not fees:
		return 0, 0.0, 0

	total = sum(fees)
	return total, total / len(fees), max(fees)
