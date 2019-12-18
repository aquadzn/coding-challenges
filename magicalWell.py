def magicalWell(a,b,n):
    s, m = 0, 0
    while m < n:
        s += a * b
        a += 1
        b += 1
        m += 1
    return s