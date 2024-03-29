#12345
#54321
#Using two pointers - take start index and end index and swap until 0

def revArray(arr):
    start = 0
    end = len(arr) - 1
    while(start<end):
        arr[start], arr[end]= arr[end], arr[start] #swapping needs to happen in the same line
        start += 1
        end -= 1
    return arr
        
print(revArray([1,2,3,4,5]))