def findUnionAndIntersection(arr1, arr2):
    unionRes = list(set(arr1) | set(arr2))
    intersectionRes = list(set(arr1) & set(arr2))
    print(intersectionRes)
    return len(unionRes), len(intersectionRes)
    
    
print(findUnionAndIntersection([1, 2, 3, 4, 5], [1, 2, 3, 7, 8]))


#The union of two given sets is the set that contains all the elements of both sets
#in Python, intersection() is a built-in set method used to find the common elements between two or more sets. 