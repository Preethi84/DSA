def getMinMax(arr):
    minele = arr[0]
    maxele = arr[1]
    if(len(arr) == 1):
        minele = arr[0]
        maxele = arr[0]
    for i in arr:
        if(i < minele):
            minele = i
        if(i > maxele):
            maxele = i
    return minele, maxele

a, b = getMinMax([100, 3, 2000, 77, 1])
print(a,b)

#improvise - linear search

#  for i in range(2, len(arr)):
#         if(arr[i] < minele):
#             minele = arr[i]
#         if(arr[i] > maxele):
#             maxele = arr[i]