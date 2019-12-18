# def fractionReducing(f):
#     return [i / math.gcd(f[0], f[1]) for i in f]

# fractionReducing = lambda f: [i / math.gcd(f[0], f[1]) for i in f]

f, = eval(dir()[0])
return [i / math.gcd(f[0], f[1]) for i in f]