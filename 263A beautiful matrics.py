c = 0
d = 0
x = 0
for i in range(1, 6):
    a = list(map(int, input().split(' ')))
    c = 0
    for j in range(len(a)):
        if a[j] == 1:
            d = i
            x = c+1
            break
        else:
            c+=1



print(abs(3 - d) + abs(3 - x))
