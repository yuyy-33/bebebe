def reorder_qty(stock, safety, lot, factor=2):
    if stock >= safety:
        return 0
    if lot <= 0:
        raise ValueError("包裝量必須大於 0")

    required = safety * factor - stock
    quantity = 0
    while quantity < required:
        quantity += lot
    return quantity


def plan(items):
    reorder_items = []
    total_amount = 0

    for name, stock, safety, lot, price in items:
        quantity = reorder_qty(stock, safety, lot)
        if quantity == 0:
            continue

        amount = round(quantity * price, 1)
        reorder_items.append((name, quantity, amount))
        total_amount += amount

    return reorder_items, round(total_amount, 1)


if __name__ == "__main__":
    assert reorder_qty(20, 10, 5) == 0
    assert reorder_qty(3, 10, 4) == 20
    assert plan([("測試品", 3, 10, 4, 2.5)]) == (
        [("測試品", 20, 50.0)],
        50.0,
    )
