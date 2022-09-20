for x in range(1, 100):
    y = 36 ** 17 - 6**x + 71
    k = 0
    while y > 0:
        k+=y % 6
        y = y // 6
    if k == 61: print(x)
