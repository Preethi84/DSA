  
# Python3 program to find large
# factorials
 
# Returns Factorial of N
def multiply(x, res, res_size):
     
    carry = 0  # Initialize carry
 
    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10  # Store last digit of
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod//10  # Put rest in carry
        i = i + 1
 
    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1
 
    return res_size
 
 
# Driver method
N = 20;
print(multiply(N));