def sort(arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range(n):
        if(arr[i]< 0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    print(pos)
    print(neg)
    if(pos > neg):
        for i in range(0, len(neg)):
            arr[2*i]= pos[i]
            arr[2*i+1]= neg[i]
        ind = len(neg)*2
        for i in range(len(neg), len(pos)):
            arr[ind] = pos[i]
            ind += 1
    else:
        for i in range(0, len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        ind = len(pos)*2
        for i in range(len(pos), len(neg)):
            arr[ind] = neg[i]
            ind += 1
        
    return arr
            
    
    
arr = [-5, -2, 5, 2, 4,
       7, 1, 8, 0, -8]
 
print("Given Array is:")
print(arr)
 
print("\nRearranged array is:")
print(sort(arr))