def halvingSum(n):
    s = 0
    while n:
        s += n
        n //= 2
    return s

# s (int) : Sum
# n (int) : Input number