def rotate_and_reverse(arr:list, k:int) -> list:

    n = len(arr)
    k = k % n

    rotated_arr = arr[n - k:] + arr[:n - k]
    reversed_arr = rotated_arr[::-1]
    return reversed_arr

