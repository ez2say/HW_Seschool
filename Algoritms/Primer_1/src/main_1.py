

def summa_of_elem(lst: list) -> int:


    sum = 0

    for i in range(0, len(lst), 1):
        if lst[i] % 2 == 0:
            sum += lst[i]
            if sum < 0:
                sum = 1

    print(sum)
    return sum





