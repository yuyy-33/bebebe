def summary(results):
    total = len(results)
    if total == 0:
        return 0, 0, 0.0

    good = results.count("OK")
    rate = good / total * 100
    return total, good, rate


def decide(rate, aql=95.0):
    return "允收" if rate >= aql else "拒收"
