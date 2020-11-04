n, t= map(int, input().split(' '))
m = input()
h = list(map(int, m.split()))
l=[]
for i in range(0, n):
    if h[i] > t:
        k=2
        l.append(k)
    else:
        p=1
        l.append(p)
print(sum(l))

