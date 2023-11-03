r,c=map(int,input().split())
l=[]
for i in range(r):
    l.extend(list(map(int,input().split())))
e=0
o=0
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
print(e,o)