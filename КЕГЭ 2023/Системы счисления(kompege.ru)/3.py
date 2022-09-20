x = 2*27**7 + 3 ** 10 - 9
k = 0
while x > 0:
    if x % 3 == 0: k+=1
    x = x // 3
print(k)
