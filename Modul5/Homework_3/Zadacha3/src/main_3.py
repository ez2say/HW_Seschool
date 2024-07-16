def reverse_even_elements(arr:list):
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    even_numbers.reverse()

    result = []
    i, j = 0, 0
    while i < len(even_numbers) or j < len(odd_numbers):
        if i < len(even_numbers):
            result.append(even_numbers[i])
            i += 1
        if j < len(odd_numbers):
            result.append(odd_numbers[j])
            j += 1

    return result

