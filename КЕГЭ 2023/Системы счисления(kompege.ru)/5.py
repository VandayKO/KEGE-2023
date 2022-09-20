for x in range(1, 1000):
    y = 125 ** 200 - 5**x +74
    k = 0
    while y > 0:
        if y % 5 == 4: k+=1
        y = y // 5
    if k == 100: print(x)
