# def gasPrediction(driveDistances, currentGasLevel, avgMileage):
#     a = sum(driveDistances) / 12 / avgMileage
#     print(a)
#     if a > currentGasLevel:
#         return True
#     else:
#         return False

# d, c, a = eval(dir()[0])
# return sum(d) / 12 / a > c

# 39 chars
gasPrediction = lambda d, c, a: sum(d) / 12 / a > c