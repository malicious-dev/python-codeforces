t = int(input())
while t:
    t = t-1
    x =input()
    s = len(x)
    count = int(((int(x[0])-1)*10) + (s*(s+1))/2)
    print(count)


