def min_help(a):
    s,c=1,1
    while a!=s:
        if s*2<=a:
            s=s*2
        else:
            s=s+1
            c+=1
    return c

a=int(input())
print(min_help(a))
