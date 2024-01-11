n=int(input())
a=list(map(int,input().split()))
s=0
m=0
for i in range(n//2):
    s+=a[i]
for j in range(n//2,n):
    m+=a[j]
print(s)
print(m)