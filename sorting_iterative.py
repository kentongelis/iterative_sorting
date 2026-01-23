#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) — checks each adjacent pair once.
    Best case O(1) if an out-of-order pair is found early.
    Memory usage: O(1) — constant extra space.
    """
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n²) — in the worst case, many passes are required and each
    pass may compare up to n adjacent pairs.
    Best case is O(n) if the list is already sorted, since only one pass is needed.
    Memory usage: O(1) — sorting is done in place using a constant amount of
    extra space"""
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


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n²) — the outer loop runs n times and the inner loop
    scans the remaining unsorted portion each time, regardless of input order.
    Best, average, and worst cases are all O(n²).
    Memory usage: O(1) — sorting is done in place using a constant amount
    of extra space.
    """
    for i in range(len(items) - 1):
        smallest_index = i

        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[i], items[smallest_index] = items[smallest_index], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n²) — in the worst case (reverse-sorted list), each item
    may need to be compared and swapped with all previous items.
    Best case: O(n) — if the list is already sorted, the inner while loop
    never runs.
    Memory usage: O(1) — sorting is done in place using a constant amount of
    extra space.
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items
