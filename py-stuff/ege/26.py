
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
