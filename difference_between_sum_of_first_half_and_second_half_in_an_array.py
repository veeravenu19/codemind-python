n=int(input())
a=list(map(int,input().split()))
s=s1=0
for i in range(n//2):
    s+=a[i]
for j in range(n//2,n):
    s1+=a[j]
print(s1-s)