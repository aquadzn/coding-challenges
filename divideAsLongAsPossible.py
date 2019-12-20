n, d = eval(dir()[0])
while n % d == 0:
    n /= d
return n

# def divideAsLongAsPossible(n, d):
#     while n % d == 0:
#         n /= d
#     return n