def countAndSay(n):
    if(n==1):
        return '1'
    if(n==2):
        return '11'
    s = '11'
    for i in range(3, n+1):
        s = s + '$'
        print(s)
        c = 1
        t = ""
        for j in range(1,len(s)):
            print(s[j])
            if(s[j]!=s[j-1]):          
                t = t + str(c) + s[j-1]
                c = 1
            else:
                c = c + 1
        s = t
    return s

print(countAndSay(4))

