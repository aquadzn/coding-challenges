L, = eval(dir()[0])
s = 0


while len(L) > 1:
    L = numpy.add(L[:-1:2], L[1::2]) if s % 2 == 0 else numpy.multiply(L[:-1:2], L[1::2])
    s += 1

return L[0]
