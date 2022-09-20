for x in range(1, 16):
    try:
        if int('33', x+4) - int("33", 4) == int("33",10): print(x)
    except:
        ...
