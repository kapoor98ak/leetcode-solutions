# Sliding Window

def res(arr, k) -> list:
    left, right, n, window_sum = 0, 0, len(arr), 0
    res = []
    while right < n:
        window_sum += arr[right]
        window_size = right - left + 1
        if(window_size >= k):
            win_avg = window_sum/k
            print(f"Window from index: {left} -to- {right} and sum: {window_sum} - avg: {win_avg}")
            res.append(win_avg)
            window_sum -= arr[left]
            left += 1
        right += 1
    return res

print(res([1, 3, 2, 6,-1, 4, 1, 8, 2], 5))