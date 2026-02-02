#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) — checks each adjacent pair once.
    Memory usage: O(1) — constant extra space.
    """
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order,
    and repeating until all items are in sorted order.

    Time Complexity is O(n^2) because every adjacent pair is checked once and after
    every swap, the index return to 0.

    Space Complexity is O(1) as it is in-place sorting
    """
    i = 0  # Start at the first index
    while i < len(items) - 1:
        num = items[i]  # Store the current item

        # Compare the current item with the next item
        if num > items[i + 1]:
            # Swap the two items if they are out of order
            items[i] = items[i + 1]
            items[i + 1] = num

            # Reset index to start over since the list may no longer be sorted
            i = 0
            continue

        # Move to the next index if no swap was needed
        i += 1

    # Return the sorted list
    return items


def selection_sort(items):
    """
    Sort given items by finding the minimum item, swapping it with the first
    unsorted item, and repeating until all items are in sorted order.

    Time Complexity is O(n^2) as the method will always look over the unsorted
    portion every time

    Space Complexity is O(1) as it is in-place sorting
    """
    # Iterate over each position in the list except the last
    for i in range(len(items) - 1):
        smallest_index = i  # Assume the current position holds the smallest item

        # Search the rest of the list for a smaller item
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j  # Update index of smallest item found

        # Swap the smallest item found with the item at position i
        items[i], items[smallest_index] = items[smallest_index], items[i]

    # Return the sorted list
    return items


def insertion_sort(items):
    """
    Sort given items by taking the first unsorted item, inserting it into
    the correct position among the already-sorted items, and repeating.

    Time Complexity is O(n^2) as it is another nested iteration

    Space Complexity is O(1) as it is still in place sorting
    """
    # Start from the second element (the first is already considered sorted)
    for i in range(1, len(items)):
        j = i  # Index of the current item to insert

        # Move the item left while it is smaller than the previous item
        while j > 0 and items[j] < items[j - 1]:
            # Swap the item with the one before it
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1  # Move left in the sorted portion

    # Return the sorted list
    return items
