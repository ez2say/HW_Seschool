def povtoryashka(lst:list) -> int:
    counts = {}
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    max_count = max(counts.values())
    most_frequent = [number for number, count in counts.items() if count == max_count]

    return min(most_frequent)



