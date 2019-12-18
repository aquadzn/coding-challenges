#def passwordCheck(s):
#    if any(i.isdigit() for i in s) and any(i.islower() for i in s) and any(i.isupper() for i in s) and len(s) >= 5:
#        return True
#    else:
#        return False

#passwordCheck = lambda s: (any(i.isdigit()) and any(i.islower()) and any(i.isupper())) for i in s and len(s) > 4

# Regex:

#def passwordCheck(s):
#    return len(s) > 4 and all(re.search(p, s) for p in ('[A-Z]', '\d', '[a-z]'))

passwordCheck = lambda s: len(s) > 4 and all(re.search(i, s) for i in ('[A-Z]', '\d', '[a-z]'))