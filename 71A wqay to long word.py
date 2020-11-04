i=input

for _ in [0]*int(i()):

    s=i();l=len(s)-2;print([s,s[0]+str(l)+s[-1]][l>8])
