i = int(input())
print(i)
k=[]
x=[]
for j in range(0, i):
    m, n = map(int, input().split())
    k.append(m)
    x.append(n)
print(k)
print(x)
f=[]
for p in range(0, i*2):
    if k[0]<x[0]:
        f.append(1)
        continue
    elif k[1]<x[1]:
        f.append(2)
        continue
    elif k[2]<x[2]:
        f.append(3)
        continue
    elif k[0] == x[0]:
        f.append(4)
        continue
    elif k[1] == x[1]:
        f.append(5)
        continue
    elif k[2] == x[2]:
        f.append(6)
print(f)
    
    


