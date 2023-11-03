r,c=map(int,input().split())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
e=0
o=0
for i in range(r):
    for j in range(c):
        if i%2==0:
            e+=l[i][j]
        else:
            o+=l[i][j]
print(e,o,end=' ')