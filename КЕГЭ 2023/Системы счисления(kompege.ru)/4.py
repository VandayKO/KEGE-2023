x = 51*7**12 - 7**3 - 22
k = 0
while x > 0:
    k+=x%7
    x = x // 7
print(k)
