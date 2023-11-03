r,c=map(int,input().split())
l=[]
for i in range(r):
    l.extend(list(map(int,input().split())))
print(sum(l))