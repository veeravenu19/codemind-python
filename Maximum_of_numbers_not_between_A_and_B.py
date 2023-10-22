n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
for i in range(b,c+1):
    if i>=b and i<=c:
        if i in a:
            a.remove(i)
        else:
            continue
if a==[]:
    print('-1')
else:
    print(max(a))