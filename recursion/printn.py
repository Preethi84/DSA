def OutN(n):
    if(n == 1):  #base case
        print(n)
        return
    print(n) #hypothesis
    OutN(n-1) #recursive case or induction case
    
OutN(10)