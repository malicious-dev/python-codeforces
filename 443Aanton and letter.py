n = input()
s=list(n)
b = []
for i in range(1, len(s), 3):
    b.append(s[i])
d=list(dict.fromkeys(b))
listToStr = ''.join([str(elem) for elem in d]) 
if (listToStr.isalpha()) != True:
    print(0)
else:
    print(len(d))
    
