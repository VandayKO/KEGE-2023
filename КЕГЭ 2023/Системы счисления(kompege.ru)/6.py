for x in range(1, 3000):
    y = 4**2015 + 2**x - 2**2015 + 15
    k = 0
    while y > 0:
        if y % 2 == 1: k+=1
        y = y // 2
    if k == 500: print(x)
