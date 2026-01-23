def selection(items):
    for i in range(len(items) - 1):
        smallest_index = i

        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[i], items[smallest_index] = items[smallest_index], items[i]
    return items


print(selection([8, 3, 1, 4, 5]))
