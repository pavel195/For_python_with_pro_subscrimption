
s1 = 'BCD'
s2 = "O"
c = 0
n = ''.join([x for x in open('24.txt')])
for i in range(len(n)-1):
    if n[i] in s1 and n[i+1] in s2:
        c+=1
print(c)



