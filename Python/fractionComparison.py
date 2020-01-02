# def fractionComparison(a, b):
#     d = a[0] / a[1]
#     f = b[0] / b[1]
#     if d < f:
#         return "<"
#     elif d > f:
#         return ">"
#     else:
#         return "="

(a, b), (c, d) = eval(dir()[0])
r = (a * d) / (b * c)
return "<" if r < 1 else ">" if r > 1 else "="

# 72 chars