
def max_in_range(arr:list[int], start:int, end:int):

    if start < 0 or end >= len(arr) or start > end:
        raise ValueError("Неверные индексы")

    max_element = arr[start]
    max_index_relative = 0
    max_index_absolute = start

    for i in range(start + 1, end + 1):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index_relative = i - start
            max_index_absolute = i

    return max_element, max_index_relative, max_index_absolute

