def insert(arr, temp):
    if(len(arr) == 0 or arr[len(arr)-1] <= temp):
        arr.append(temp)
        return 
    v = arr[len(arr)-1]
    arr.pop()
    insert(arr, temp)
    arr.append(v)
    
def sort(arr):
    if(len(arr) <= 1):
        return arr
    temp = arr[len(arr)-1]
    arr.pop()
    sort(arr)
    insert(arr, temp)
    return arr

arr = [1,2,4,5,3]
print(sort(arr))