# def insertDashes(s):
#     return "-".join(s).replace("- -", " ")
# 55

# insertDashes = lambda s: "-".join(s).replace("- -", " ")
# 51

# return "-".join(*eval(dir()[0])).replace("- -", " ")
# 50

return re.sub("- -", " ", "-".join(*eval(dir()[0])))
# 49