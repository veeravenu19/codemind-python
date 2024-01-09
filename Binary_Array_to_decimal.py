n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    n=n-1
    s+=i*2**n
print(s)