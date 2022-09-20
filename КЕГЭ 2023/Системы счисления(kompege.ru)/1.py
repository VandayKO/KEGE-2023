x = 64**30 + 2**300 - 4
k = 0
while x > 0:
    if x%8 == 7: k+=1
    x = x // 8
print(k)
