from math import ceil
f=open('27_A.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append([int(x) for x in f.readline().split()])
m = 10**20
p=0
for i in range(n):
    s = 0
    for j in range(n):
        k = ceil(a[i][1]/36)
        r = abs(a[i][0]-a[j][0])
        s += r*k
    if s < m :
        m = s
        p=i
print(p,' ',m)
