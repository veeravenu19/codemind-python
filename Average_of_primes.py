def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
n=list(map(int,input().split()))
l=[]
for i in n:
    if prime(i):
        l.append(i)
a=sum(l)/len(l)
print("%.2f"%a)