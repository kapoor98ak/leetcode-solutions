
def removeDuplicates(arr):
    res = len(arr)

    for i in range(len(arr)-1):
        print(i, ' - ', arr[i])
        if(arr[i] == arr[i+1]):
            res -= 1 
    print(arr)
    return res




print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
# print(removeDuplicates([2, 2, 2, 11]))