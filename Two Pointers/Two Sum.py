def result(arr: list, target: int) -> list:
    left_ptr = 0
    right_ptr = len(arr)-1
    while(left_ptr <= right_ptr):
        pair_sum = arr[right_ptr] + arr[left_ptr]
        if(pair_sum > target):
            right_ptr -= 1
        elif(pair_sum < target):
            left_ptr += 1
        elif(pair_sum == target):
            return list([left_ptr, right_ptr])
    
    return list([])

print(result([1, 2, 3, 4, 6], 6))
print(result([2, 5, 9, 11], 11))

