def maxSubarray(A):
    # A: inputArray
    # m: Max
    # 
    # 
    m = e = 0
    for i in A:
        e += i
        if e < 0:
            e = 0
        if m < e:
            m = e
    return m