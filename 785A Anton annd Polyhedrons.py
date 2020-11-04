n = int(input())


p=[]
for i in range(0, n):
    m= list(input())
    k=""
    l=k.join(m)
    p.append(l)
j=[]
for i in range(0, n):
    if p[i]=='Tetrahedron':
        r=4
        j.append(r)
    elif p[i]=='Cube':
        r=6
        j.append(r)
    elif p[i]=='Octahedron':
        r=8
        j.append(r)
    elif p[i]=='Dodecahedron':
        r=12
        j.append(r)
    elif p[i]=='Icosahedron':
        r=20
        j.append(r)
print(sum(j))
    
