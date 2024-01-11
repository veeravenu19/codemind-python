n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in a:
    if a.count(i)==i and i not in l:
        l.append(i)
    else:
        c+=1
if c==len(a):
    print(-1)
else:
    print(*l)