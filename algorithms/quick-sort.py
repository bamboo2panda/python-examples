def quicksort(arr):
    qs(arr, 0, len(arr) - 1)

def qs(arr: list, l: int, r: int) -> list:
    if l >= r:
        return arr
    p = partition(arr, l, r)
    qs(arr, l, p - 1)
    qs(arr, p + 1, r)
    
def partition(arr: list, l: int, r:int) -> int:
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    
    return i + 1


test_array = [-2, 6, 10, 5, -30, 2, 0, 11]
quicksort(test_array)
print(test_array)


a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = []
a4 = [3, 1, -1, 0, 2, 5]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]

quicksort(a1)
quicksort(a2)
quicksort(a3)
quicksort(a4)
quicksort(a5)
quicksort(a6)
quicksort(a7)
quicksort(a8)
quicksort(a9)

assert a1 == [1, 2, 3]
assert a2 == [1, 2, 3]
assert a3 == []
assert a4 == [-1, 0, 1, 2, 3, 5]
assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
assert a6 == [0]
assert a7 == [-2, -1, 0, 1, 2, 3, 4]
assert a8 == [1, 2, 3, 4, 5, 6, 7]
assert a9 == [2, 2, 2, 2, 2, 2, 2]








def func(number: str) -> str:
    numbers_list = list(numbers)
    number_of_tail_nines = 0
    while i in range(len(numbers_list)):
        if numbers_list[-i] == 9:
            number_of_tail_nines = i
    start = a[:len(numbers_lnumberist)-i]
    end = int(a[:-])
    end += 1
    return start + end


def func(number: str) -> str:
    numbers_list = list(numbers)
    number_of_tail_nines = 0
    while i in range(1, len(numbers_list) + 1):
        if numbers_list[-i] == '9':
            number_of_tail_nines = i
    start = numbers_list[:len(numbers_list)-number_of_tail_nines]
    end = int(numbers_list[:-number_of_tail_nines])
    end += 1
    return start + end