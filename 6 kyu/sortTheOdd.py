def sort_array(source_array):
    odds = []
    indexes = []

    for i in range(len(source_array)):
        if source_array[i] % 2:
            odds.append(source_array[i])
            indexes.append(i)

    odds = sorted(odds)

    for i in range(len(indexes)):
        source_array[indexes[i]] = odds[i]

    return source_array
