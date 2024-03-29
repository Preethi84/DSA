def minMaxHeights(arr,n,k):
    arr.sort()
    ans = arr[n-1] - arr[0]
    minim = arr[0]
    maxim = arr[n-1]
    for i in range(1,n):
        if(arr[i] < k):
            continue
        minim = min(minim + k, arr[i]-k)
        maxim = max(maxim - k, arr[i-1]+k)
        ans = min(ans, maxim-minim)
    return ans
    
    
print(minMaxHeights([5, 1, 2, 9, 4, 10], 6,1))

