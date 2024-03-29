import math


# Найти подмассив с максимальной суммой
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


def find_max_substraction_subarray(arr: list) -> int:
    max_value = 0
    current_running_summ = 0
    window_start_index = 0
    for index, item in enumerate(arr):
        current_running_summ = item - arr[window_start_index]
        if index

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


# Найти симую длинную последовательность из n букв

def find_longest_sequence(arr: list, length: int) -> int:
    longest_subsiquence = 0
    window_start_index = 0
    char_frequancy_map = {}
    for window_end_index, window_end_value in enumerate(arr):
        char_frequancy_map.update({window_end_value: char_frequancy_map.get(window_end_value, 0) + 1})
        
        while(len(char_frequancy_map) > length):
            print(char_frequancy_map)
            left_char = arr[window_start_index]
            char_frequancy_map.update({left_char: char_frequancy_map.get(left_char) - 1})
            if char_frequancy_map.get(left_char) == 0:
                char_frequancy_map.pop(left_char)
            window_start_index += 1
        longest_subsiquence = max(longest_subsiquence, window_end_index - window_start_index + 1)
    return longest_subsiquence


print (find_longest_sequence(['a', 'a', 'a', 'h', 'h', 'i', 'b', 'c'], 2))