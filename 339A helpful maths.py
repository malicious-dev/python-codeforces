i = list(input())
a=[]
for j in range(0, len(i), 2):
    a.append(i[j])
c=sorted(a)
b="+"
b=b.join(c)
print(b)
