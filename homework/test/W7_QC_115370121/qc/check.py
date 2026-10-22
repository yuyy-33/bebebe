def judge(value, target, tol=0.05):
    deviation = round(value - target, 3)
    if deviation > tol:
        return "偏大"
    if deviation < -tol:
        return "偏小"
    return "OK"


if __name__ == "__main__":
    samples = [
        (25.00, 25.00, 0.05, "OK"),
        (25.08, 25.00, 0.05, "偏大"),
        (24.94, 25.00, 0.05, "偏小"),
        (25.05, 25.00, 0.05, "OK"),
    ]
    for value, target, tol, expected in samples:
        result = judge(value, target, tol)
        print(f"{value} -> {result} ({'OK' if result == expected else 'FAIL'})")
