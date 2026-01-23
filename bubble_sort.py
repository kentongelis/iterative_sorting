def bubble(items):
    i = 0
    while i < len(items) - 1:
        num = items[i]
        if num > items[i + 1]:
            items[i] = items[i + 1]
            items[i + 1] = num
            i = 0
            continue
        i += 1
    return items


print(bubble([8, 3, 1, 4, 5]))
