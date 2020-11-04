n = list(input())
m="".join(n)




def Count(m):
    upper, lower = 0, 0

    for i in range(len(m)):
        if m[i].isupper():
            upper+=1
        else:
            lower+=1
    if 's' in n or 'S' in n:
    
        if upper > lower:
            print(m.upper())
        elif lower > upper:
            print(m.lower())
        else:
            print(m.lower())
    else:
        if upper > lower:
            print(m.upper())
        elif upper == lower:
            print(m.lower())
        else:
            print(m.lower())
        


Count(m)
