n, x, y = input().split()

n=int(n)//2
if ((int(x)==n or int(x) == n+1) and (int(y) == n or int(y) == n+1)):
    print("NO")
else:
    print("YES")


