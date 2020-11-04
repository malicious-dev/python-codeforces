x, y, z = map(int, input().split())
m=0
for i in range(1, z+1): 
    i*=x
    m+=i
if y >= m:
    print(0)
else:
    
    print(m-y)
