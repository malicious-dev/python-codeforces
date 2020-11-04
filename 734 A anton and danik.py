i = int(input())
j = input()
k = j.count('A')
x = j.count('D')
if k > x:
    print("Anton")
elif x==k:
    print("Friendship")
else:
    print("Danik")
