#012345
#01234
#0123
#012
#01

#one
n=6
for i in range(n,1,-1):
    b=0
    for j in range(i):
        print(b,end='')
        b = b + 1
    print()
    
    
#two
n=6
for i in range(n,1,-1):
    for j in range(0, i):
        print(j,end='')
    print()