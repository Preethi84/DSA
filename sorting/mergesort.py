
def merge(arr, lb, mid, ub):
    i = lb
    j = mid + 1
    k = lb
    b = [0]*5
    while(i<=mid and j<=ub):
        if(arr[i] <= arr[j]):
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1
    while(i <= mid):
        b[k] = arr[i]
        i += 1
        k += 1
    while(j <= ub):
        b[k] = arr[j]
        k += 1
        j += 1
    for i in range(len(arr)):
        print(i)
        arr[i] = b[i]

def mergesort(arr, lb, ub):
    print(lb, ub)
    if(lb < ub):
        mid = (lb + ub)//2
        mergesort(arr, lb, mid)
        mergesort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)

arr = [3,2,4, 1,5]
n = len(arr)
mergesort(arr, 0, n-1)
print("sorted Array:", arr)