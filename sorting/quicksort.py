
def partitionFun(arr, low, high):
    pivot = arr[low]
    start = low 
    end = high
    while start <= end:
            # It indicates we have already moved all the elements to their correct side of the pivot
        while start <= end and arr[end] >= pivot:
            end = end - 1
 
        # Opposite process
        while start <= end and arr[start] <= pivot:
            start = start + 1
 
        # Case in which we will exit the loop
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            # The loop continues
        else:
            # We exit out of the loop
            break
    arr[low], arr[end] = arr[end], arr[low]
    return end
        

def quicksort(arr, low, high):
    if(low<high):
        partition = partitionFun(arr, low, high)
        quicksort(arr, low, partition-1)
        quicksort(arr, partition+1, high)


arr = [7,6,10,5,9,2,1,15,7]
n = len(arr)
quicksort(arr, 0, n-1)
print("sorted Array:", arr)