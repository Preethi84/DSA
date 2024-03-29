def rotate(arr, n):
    last_el = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_el
    print(arr)
    
rotate([1,2,3,4,5], 5)