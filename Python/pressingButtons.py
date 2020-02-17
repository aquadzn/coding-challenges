import itertools as i

# *re.findall('...', 'abcdefghijklmno')
# >>> 'abc', 'def', 'ghi', 'jkl', 'mno'

# [0,0,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"] 
return ["".join(s) for s in i.product(*['0 0 abc def ghi jkl mno pqrs tuv wxyz'.split()[int(i)] for i in eval(dir()[0])[0]]) if s]
