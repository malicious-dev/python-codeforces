n = int(input())
for i in range(0, n):
    n, m = map(int, input().split())
    if n%m == 0:
        print(0)
    else:
        x=n%m
        ans = m-x
        print(ans)

