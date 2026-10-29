def load_items(path):
    items = []
    format_errors = 0

    with open(path, "r", encoding="utf-8") as file:
        next(file, None)
        for line in file:
            fields = line.strip().split(",")
            if len(fields) != 5:
                format_errors += 1
                continue

            name, stock_text, safety_text, lot_text, price_text = fields
            try:
                stock = int(stock_text)
                safety = int(safety_text)
                lot = int(lot_text)
                price = float(price_text)
            except ValueError:
                format_errors += 1
                continue

            items.append((name, stock, safety, lot, price))

    return items, format_errors
