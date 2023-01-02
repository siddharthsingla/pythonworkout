import decimal
def fpsum(s1, s2):
    d1 = decimal.Decimal(s1)
    d2 = decimal.Decimal(s2)
    return float(d1 + d2)

print(fpsum('123.1', '.9'))