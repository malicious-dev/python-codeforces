limit = int(input())
space = '  '
for i in range(0, limit + 1):
    print(space * (limit - i), end='')
 
    for j in range(2 * i + 1):
        if j > i:
            print(i - (j - i), end=' ')
        else:
            print(j, end=" ")
    print()
 
 
for i in range(0, limit)[::-1]:
    print(space * (limit - i), end='')
 
    for j in range(2 * i + 1)[::-1]:
 
        if j > i:
            print(i - (j - i), end=' ')
        else:
            print(j, end=" ")
    print()
