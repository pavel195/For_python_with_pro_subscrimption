path= '27_B.txt'
nn = 109
n= 0
i = 0
m = 0
m2 = 1000000000
with open(path) as f :
    s = f.readline()
    n = int(s)
    while i < n:
        s = f.readline()
        elem = [int(x) for x in s.split()]
        n1 = max(elem)
        m += n1
        for j in elem:
            if n1 != j:
                d1 = n1 - j
                if d1 % nn != 0:
                    m2 = min(m2,d1)
        i += 1
    if m % nn == 0:
        m -= m2
    print(m)






