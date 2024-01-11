n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=0
for i in a:
    if i<=k:
        l+=i
print(l)