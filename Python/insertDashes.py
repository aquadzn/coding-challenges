# def insertDashes(s):
#     return "-".join(s).replace("- -", " ")
# 55

# insertDashes = lambda s: "-".join(s).replace("- -", " ")
# 51

# return "-".join(*eval(dir()[0])).replace("- -", " ")
# 50

# return re.sub("- -", " ", "-".join(*eval(dir()[0])))
# 49

# insertDashes = lambda s: re.sub('\B', '-', s)
# 39

return re.sub('\B', '-', *eval(dir()[0]))
# 38
