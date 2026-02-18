# def res(arr: list, s: int) -> int:
#     l, r, n = 0, 0, len(arr)
#     res = n
#     print(arr)
#     window_sum, window_size = 0, 0
#     while(r < n):
#         window_sum += arr[r]
#         window_size = r-l+1
#         print(f'window -> l = {l} ; r = {r} ; window_sum = {window_sum}')
#         if(window_sum >= s):
#             res = min(res, window_size)
#             # print(f'\tupdating res - window_size: {window_size} & res: {res} & window_sum: {window_sum}')
#             while(window_sum >= s and l <= r):
#                 l+=1
#                 window_sum-=arr[l]
#                 res = min(res, window_size)
#                 print(f'\t\tupdating res - window_size: {window_size} & res: {res} & window_sum: {window_sum}')
#                 print(f'\t\tupdated window -> l = {l} ; r = {r} ; window_sum = {window_sum}')
#         r += 1
#     return res

def res(arr: list, s: int) -> int:
    win_start, win_end, arr_len = 0, 0, len(arr)
    result = arr_len
    window_sum, window_size = 0, 0
    
    while(win_end < arr_len):
        window_sum += arr[win_end]
        print(f'{win_start} -to- {win_end} -window_sum- {window_sum}')
        
        while(window_sum >= s and win_start<=win_end):
            window_size = win_end - win_start + 1
            result = min(result, window_size)

            win_start+=1
            window_sum-=arr[win_start]

            
            print(f'\t updated: {win_start} -to- {win_end} -window_sum- {window_sum}')
            
        win_end+=1

    return result

print(res([2, 1, 5, 2, 3, 2], 7))