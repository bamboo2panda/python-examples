import math


# Найти максимальную подмассив с максимальной суммой
def find_max_subarray(arr: list, length: int) -> int:
    max_value = -math.inf
    current_running_summ = 0
    for index, item in enumerate(arr):
        current_running_summ += item
        if index >= length - 1:
            max_value = max(max_value, current_running_summ)
            current_running_summ -= arr[index - (length -1)]
    return max_value

print (find_max_subarray([4, 2, 1, 7, 8, 1, 0], 3))


# Найти минимальную длину массива, с суммой >= s

def find_min_subarray_length(arr: list, target_sum: int) -> int:
    min_length = len(arr)
    corrent_window_sum = 0
    window_start_index = 0
    for window_end_index, window_end_value in enumerate(arr):
        corrent_window_sum += window_end_value
        while(corrent_window_sum >= target_sum):
            min_length = min(min_length, window_end_index - window_start_index + 1)
            corrent_window_sum -= arr[window_start_index]
            window_start_index += 1
    return min_length

print(find_min_subarray_length([4, 2, 1, 7, 8, 1, 0], 8))