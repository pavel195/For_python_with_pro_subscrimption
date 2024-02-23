from math import ceil
f=open('27_B.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append([int(x) for x in f.readline().split()])
m = 10**20
i = n//2
d=0
while i>=0 and i<n:
    s1 = 0
    s2 = 0
    for j in range(n):
        k = ceil(a[i][1]/36)
        r = abs(a[i][0]-a[j][0])
        if j<i:
            s1 += r*k
        elif j>i:
            s2 += r*k
    m = s1+s2
    if s1<s2:
        if d ==2: break
        if i == n//2: d=1
        i+=1
    else:
        if d ==1: break
        if i == n // 2: d = 2
        i-=1
p = i
if d == 1 and a[i][0] < a[i+1][0]:
    p = i+1
elif d == 2 and a[i][0] < a[i-1][0]:
    p = i-1

print(p,' ',m)
