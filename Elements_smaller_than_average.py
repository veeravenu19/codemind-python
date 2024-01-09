n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
c=0
for i in a:
    if avg>=i:
        c+=1
print(c)