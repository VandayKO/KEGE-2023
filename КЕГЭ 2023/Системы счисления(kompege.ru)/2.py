x = 3 * 16**8 - 4 ** 5 + 3
k = 0
while x > 0:
    if x % 4 == 3: k+=1
    x = x // 4
print(k)
