def sortArr(arr):
    j = 0
    for i in range(len(arr)):
        if(arr[i]<0):
            temp = arr[i]
            arr[i]  = arr[j]
            arr[j] = temp
            j = j + 1
    return arr
    
    
print(sortArr([-1,-2,0,3,-4,-9,0,13,14,-111,0]))