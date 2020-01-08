# 52
# def triangleExistence(t):
#     t.sort()
#     return t[0] + t[1] > t[2]

# 46
# triangleExistence = lambda t: sum(t) - max(t) > max(t)

# 45
# t, = eval(dir()[0])
# 
# t.sort()
# return t[0] + t[1] > t[2]

# 43
# t, = eval(dir()[0])
# return sum(t) - max(t) > max(t)

# 40 
a, b, c = sorted(*eval(dir()[0]))
return a + b > c
