def findDuplicate(arr,n):
    n = len(arr)
    freq = [0] * (n + 1)
    for i in range(n):
        if(freq[arr[i]] == 0):
            freq[arr[i]] += 1
        else:
            return arr[i]
    
print(findDuplicate([1,2,3,5,3], 5))