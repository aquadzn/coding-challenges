n, = eval(dir()[0])
r = ""

while n:
    n -= 1
    r = chr(n % 26 + 65) + r
    n //= 26
return r
