#1
#234
#56789

rows = 3
a=1
stop=2
for i in range(rows):
    for j in range(1, stop):
        print(a,end='')
        a=a+1
    stop=stop+2
    print()