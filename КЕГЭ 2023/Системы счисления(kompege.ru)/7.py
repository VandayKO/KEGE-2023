for x in range(1, 3000):
    y = 4 ** 1014 - 2**x + 12
    k = 0
    while y > 0:
        if y % 2 == 0: k+=1
        y = y // 2
    if k == 2000: print(x)
