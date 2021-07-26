def max_profit(arr: list[int], cost: int) -> int:
    i = 0
    min_value = arr[0]
    max_value = arr[0]
    max_profit = 0
    while i < len(arr) - 1:
        while i < len(arr) - 1 and arr[i] >= arr[i + 1]:
            i += 1
        min_value = arr[i]
        while i < len(arr) - 1 and arr[i] <= arr[i + 1]:
            i +=  1
        if max_value - cost > 0:
            max_profit += max_value - min_value
    return max_profit

print(max_profit([1,3,2,8,4,9], 2))