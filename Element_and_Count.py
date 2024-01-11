n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i not in l:
        print(i,a.count(i),end=' ')
    l.append(i)