# def countSumOfTwoRepresentations3(n, l, r):
#     if r < n // 2 or l > n // 2:
#         return 0
#     return n // 2 - max(l, n-r) + 1
# 87

# countSumOfTwoRepresentations3 = lambda n, l, r: max(n // 2 - max(l, n-r) + 1, 0)
# 66

n, l, r = eval(dir()[0])
return max(n // 2 - max(l, n-r) + 1, 0)
# 50