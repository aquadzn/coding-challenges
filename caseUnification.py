def caseUnification(s):
    u = (sum(1 for x in s if x.isupper()))
    if u > (len(s)/2):
        return s.upper()
    else:
        return s.lower()