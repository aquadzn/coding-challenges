l, s = eval(dir()[0])
r = []
c = 1
    
t = [[int(s[i:i+2]) for i in [1, 4]] +[s[7:9]] for s in l]
t = [f"{x // 60:02d}:{x % 60:02d}:{y:02d},{z.ljust(3, str(0))}" for x, y, z in t] + [s + ',000'] # if I replace str(0) with '0', this increases to 359 characters wtf
    
for a, b in enumerate(l):
    r.extend([str(c), t[a] + ' --> ' + t[a+1], b[11:], ''])
    c += 1
return r[:-1]
