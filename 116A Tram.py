n = int(input())
m = 0
s = 0
while n:
	x,y= map(int, input().split())
	s=s+y-x
	if s >m:
		m = s
	n=n-1
print(m)
