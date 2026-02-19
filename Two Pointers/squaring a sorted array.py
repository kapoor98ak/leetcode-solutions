# squaring a sorted array

def func(arr):
    res = []
    left, right = 0, len(arr)-1
    while(left <= right):
        if (left**2 <= right**2):
            res.append(left**2)
            left+=1
        elif (left**2 > right**2):
            res.append(right**2)
            right-=1
    return res

print(func([-4,-1,0,3,10]))