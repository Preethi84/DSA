def sort012(arr,n):
        # code here
        low = 0
        mid = 0
        high = n - 1
        while(mid <= high):
            if(arr[mid] == 0):
                temp = arr[low]
                arr[low] = arr[mid]
                arr[mid] = temp
                low = low + 1
                mid = mid + 1
            elif(arr[mid] == 1):
                mid = mid + 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high = high - 1
        return arr
                
print(sort012([1,1,0,2,2,0], 6))