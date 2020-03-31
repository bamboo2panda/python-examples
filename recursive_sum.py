arr = [5, 4, 6, 10]


def recursive_search(a: list):
    s = 0
    if len(a) > 1:
        s += a.pop(0) + recursive_search(a)
    if len(a) == 1:
        s += a.pop(0)
    return s


print(recursive_search(arr[:]))


def max_value(a: list):
    m = 0
    if len(a) > 1:
        if m < int(a.pop(0)):
            m = max_value(a)
    if len(a) == 1:
        m = a.pop(0)
    return m


print(max_value(arr[:]))

