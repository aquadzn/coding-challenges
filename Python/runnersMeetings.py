p, s = eval(dir()[0])
r = -1
l = len(p)
for i in range(l):
    for j in range(l):
        c = 0
        d = p[j] - p[i]
        f = s[i] - s[j]

        if d * f < 1:
            continue

        for k in range(l):
            if p[k] * f + s[k] * d == p[i] * f + s[i] * d:
                c += 1
        if c > r:
            r = c
return r