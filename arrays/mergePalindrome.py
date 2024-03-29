def mergePalindrome(arr, n):
    i = 0
    j = n - 1
    ans = 0
    while i <= j:
        if(arr[i] == arr[j]):
            i = i + 1
            j = j - 1
        elif(arr[i] > arr[j]):
            j = j - 1
            arr[j] = arr[j+1] + arr[j]
            ans += 1
        else:
            i = i + 1
            arr[i] = arr[i-1] + arr[i]
            ans += 1
    print(arr)
    return ans

print(mergePalindrome([1,3,7,3,9],5))