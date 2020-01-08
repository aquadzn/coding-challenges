# 134
L, = eval(dir()[0])
s = 0

while len(L) > 1:
    if s % 2 == 0:
        L = [a + b for a, b in zip(L[:-1:2], L[1::2])]
    else:
        L = [a * b for a, b in zip(L[:-1:2], L[1::2])]
    s += 1

return L[0]
