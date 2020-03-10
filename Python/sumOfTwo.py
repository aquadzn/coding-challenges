def sumOfTwo(a, b, v):
    b = set(b)
    return any(v - i in b for i in a)
