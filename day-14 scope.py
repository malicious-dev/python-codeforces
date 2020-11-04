a=int(input())
b=list(map(int, input().split()))

print(a)
print(b)
k=[]
for i in range(0, a):
    if b[i] < b[-1]:
        p=b[-1]-b[i]
        k.append(p)
    else:
        k.append(p)

print(max(k))
