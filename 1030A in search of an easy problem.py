i = int(input())

j = list(map(int, input().split()))
p=j.count(1)
if p >= 1:
    print("HARD")
else:
    print("EASY")
