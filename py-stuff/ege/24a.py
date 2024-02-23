import re
n = ''.join([x for x in open('24(1).txt')])
c='(AB)+'

r = re.findall(c,n)
print(r)