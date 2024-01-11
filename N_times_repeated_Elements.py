n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=[]
c=0
for i in a:
    if a.count(i)==k and i not in l:
        print(i,end=' ')
        l.append(i)
    else:
        c+=1
if c==len(a):
    print(-1)