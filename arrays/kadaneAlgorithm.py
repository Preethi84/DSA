def largestSumSubarry(arr):
    max_sum = arr[0]
    curr_sum = 0
    for i in arr:
        curr_sum = curr_sum + i
        if(max_sum < curr_sum):
            max_sum = curr_sum
        if(curr_sum < 0):
            curr_sum = 0
    return max_sum, curr_sum
    
    
print(largestSumSubarry([-2, -3, 4, -1, -2, 1, 5, -3]))