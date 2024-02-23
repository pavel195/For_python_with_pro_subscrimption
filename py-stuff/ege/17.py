from functools import lru_cache
n = [int(x) for x in open('17(4).txt')]
c=m=0
@lru_cache(None)
def f(n):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]*n[j]%14!=0:
                c+=1
                m = max(m,n[j]+n[i])

print(f"m = {m} c - {c}")