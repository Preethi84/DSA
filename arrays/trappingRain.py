def trappingRain(arr,n):
    if n < 3:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    res = 0
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1],arr[i])
    right_max[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        right_max[j] = max(right_max[j+1], arr[j])
    for i in range(n):
        res += min(left_max[i], right_max[i]) - arr[i]
    return res
        


arr = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len(arr)
print(trappingRain(arr,n))