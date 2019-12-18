def visitsOnCircularRoad(n, v):
    c = 1
    t = 0
    for i in v :
        t += min(abs(i - c), abs(n - abs(i - c)))
        c = i
    return t

# v = visitsOrder
# n = number of houses
# c = Current position
# t = Time