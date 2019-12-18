#def smallestMultiple(l, r):
#    for i in range(1,8**7):
#        s = True
#        for j in range(l, r+1):
#            if i%j!=0:
#                s = False
#        if s:
#            return i

def smallestMultiple(l ,r):
    for i in range(1, 16):
        for j in range(l, r+1):
            while True:
                if i % j != 0:
                    break
            return i