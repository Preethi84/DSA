#brute force approach

def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]
    
    
print(kthSmallest([10, 2, 33, 56, 89], 5))