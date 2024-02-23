def f(a,b):
    if a<b:
        return 0
    elif a==b:
        return 1
    else:
        return f(a-1,b)+f(int(a/2),b)
print(f(32,13)*f(13,1))

