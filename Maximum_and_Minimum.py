n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    if a.count(i)==i:
        l.append(i)
    else:
        c+=1
if c==len(a):
    print(-1)
else:
    print(min(l),max(l))