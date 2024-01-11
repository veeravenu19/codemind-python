n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
l=[]
for i in a:
    if i>=b and i<=c:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(max(l))