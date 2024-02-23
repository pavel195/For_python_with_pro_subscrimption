--------------- 19 – 21 --------------------------------------
from functools import lru_cache
def moves(a):
    return a+1,a*3-2
@lru_cache(None)
def game(h):
    if h > 30:
        return "win"
    if any(game(m) == 'win' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'v1'
    if any(game(m) == 'v1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(h)):
        return 'v2'
for i in range(3,13):
    print(i, ' ', game(i))

--------------  26 --------------------------------
f= open('26.txt')
n = int(f.readline())
a = [int(f.readline()) for x in range(n)]

a = sorted(a)[::-1]
m = a[0]
c = 1
for i in range(n):
    if m-a[i]>=3:
        c+=1
        m = a[i]
print(c,m)


-------------------27------------------------------------
from math import ceil
f= open('27(8).txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append([int(x) for x in f.readline().split()])
m = 10**20
for i in range(n):
    s = 0
    for j in range(n):
        k = ceil(a[i][1]/36)
        r = abs(a[i][0]-a[j][0])
        s += r*k
    if s < m :
        m = s
print(m)

