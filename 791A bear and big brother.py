i, j = map(int, input().split())
m=1
for k in range(0, 999):
    i*=3
    j*=2
    if i > j:
        print(m)
        break
    m+=1
    
