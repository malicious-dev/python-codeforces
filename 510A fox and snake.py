n, m = map(int, input().split())
for i in range(1, n+1):
    if i==1:
        print("#"*m)
        continue
    elif i %2 == 0 and (i % 4) != 0:
        print("."*(m-1)+"#")
        continue
    elif i % 2 != 0:
        print("#"*m)
        continue
    elif i % 4 == 0:
        print("#"+"."*(m-1))

        

